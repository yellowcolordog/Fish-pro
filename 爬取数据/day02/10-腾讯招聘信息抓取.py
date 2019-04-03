import random
import requests
import pymysql
import re
from urllib import parse
import time

useragents = [
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'},
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'},
    {'User-Agent':'Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50'},
    {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; ) AppleWebKit/534.12 (KHTML, like Gecko) Maxthon/3.0 Safari/534.12'},
    {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.33 Safari/534.3 SE 2.X MetaSr 1.0'},
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 QQBrowser/6.9.11079.201'},
]
# https://hr.tencent.com/position.php?keywords=&tid=0&lid=2268&start=0#a
# https://hr.tencent.com/position_detail.php?id=41853&keywords=&tid=0&lid=2268
# 职位名称 	职位类别 	人数 	地点 	发布时间
class TencentSpider(object):
    def __init__(self):
        self.baseurl='https://hr.tencent.com/position.php'
        self.db = pymysql.connect('localhost','root','123456',charset='utf8')
        self.cursor = self.db.cursor()
        

    def get_page(self,url):
        headers = random.choice(useragents)
        # print(headers['User-Agent'])
        res = requests.get(url,headers=headers)
        res.encoding='utf-8'
        html = res.text
        return html
        

    def parse_html(self,html):
        p1 = re.compile(r'<td class="l square">.*?href="(.*?)">(.*?)</a>.*?</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>',re.S)
            # <tr class="even">
            #   <td class="l square"><a target="_blank" href="position_detail.php?id=46719&amp;keywords=python&amp;tid=87&amp;lid=2268">CSIG15-自然语言研究员</a></td>
            #   <td>技术类</td>
            #   <td>1</td>
            #   <td>成都</td>
            #   <td>2019-04-02</td>
            # </tr>
            # <tr class="odd">
            #     <td class="l square"><a target="_blank" href="position_detail.php?id=46711&amp;keywords=python&amp;tid=87&amp;lid=2268">CSIG15-自然语言处理工程师</a></td>
            # 		<td>技术类</td>
            # 		<td>1</td>
            # 		<td>成都</td>
            # 		<td>2019-04-02</td>
            #   </tr>
            # r'<td class="l square">.*?href="(.*)">(.*?)</a>.*?</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>'
        l = p1.findall(html)

        p2 = re.compile(r'class="lightblue">工作职责：.*?ass="squareli">(.*?)</ul>.*?class="lightblue">工作要求：.*?ass="squareli">(.*?)</ul>',re.S)
            # <td colspan="3" class="l2">
            #   <div class="lightblue">工作职责：</div>
            #   <ul class="squareli">
            #     <li>负责移动游戏自动化测试工具的开发、维护和完善；</li>
            #     <li>负责移动游戏专项测试工具的开发、用例设计和测试执行；</li>
            #     <li>负责游戏整体的质量把控，制定测试方案、计划、跟踪实施，监控项目外网质量并实施改进； </li>
            #     <li>负责收集和分析业务测试需求，探索更多的测试手段和维度，帮助提升部门的测试质量、效率和深度。</li>
            #   </ul>
            # </td>
        return l

    def write_page(self,r_list):
        for r_set in r_list:
            ins = 'insert into tencent(href,name,type,count,place,update_time) values("%s","%s","%s","%s","%s","%s");'%r_set
            try:
                self.cursor.execute(ins)
                self.db.commit()
            except Exception as e:
                print(e)
                print(ins)
                self.db.close()

    def work_on(self):
        # ?keywords=&tid=0&lid=2268&start=0#a
        page=1
        self.cursor.execute('use AID1811db')
        while 1:
            start=(page-1)*10
            canshu = '?keywords=&tid=0&lid=2268&start=%s'%start #?keywords=&tid=0&start=10#a
            url = self.baseurl+canshu
            html = self.get_page(url) # 获取html页面
            r_list = self.parse_html(html) # 获取需要的数据p1?,列表格式
            if not r_list:
                print(url)
                break
            self.write_page(r_list) # 将数据存进数据库
            print('第%s页抓取成功'%page)
            time.sleep(random.random()*1)
            page+=1
        self.db.close()


spider = TencentSpider()
spider.work_on()