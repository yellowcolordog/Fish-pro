# 1. 把百度贴吧案例重写一遍
# 2. 爬取猫眼电影信息: 猫眼电影 - 榜单 - top100榜
#    猫眼电影 - 第1页.html
#    猫眼电影 - 第2页.html
#    ...
# 3. 正则回顾, mysql和mongDB基本命令回顾

import urllib.request
import urllib.parse
import random
import time 

useragents = [
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'},
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'},
    {'User-Agent':'Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50'},
    {'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)'},
    {'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'},
]

class Tieba:
    def __init__(self):
        self.baseurl='http://tieba.baidu.com/?'
        self.header = random.choice(useragents)
    
    # 获取地址
    def get_url(self,url,headers):
        req = urllib.request.Request(self.baseurl,headers=self.header)
        res = urllib.request.urlopen(req)
        html = res.read().decode()
        return html
    # 保存数据
    def save_html(self,html,filename):
        # 保存路径
        ab_file = '/home/tarena/正式课/爬虫/day01/file/'+filename
        with open(ab_file,'wt') as f:
            f.write(html)

    # 主函数
    def run(self):
        name = input('请输入贴吧名称:')
        start = int(input('请输入起始页:'))
        end = int(input('请输入终止页:'))
        # for 循环拼接URL地址, 发请求
        for page in range(start,end+1):
            headers=random.choice(useragents)
            pn = (page-1)*50
            canshu = urllib.parse.urlencode({
                "kw":name,
                'pn':pn,
            })
            url = self.baseurl + canshu
            req = urllib.request.Request(url,headers=headers)
            res = urllib.request.urlopen(req)
            html = res.read().decode()
            filename = '%s的第%s页.html'%(name,page)
            self.save_html(html,filename)
            print('第%s页爬取成功'%page)
            time.sleep(5/10)

tieba = Tieba()
# tieba.run()

class Maoyan:
    def __init__(self):
        self.baseurl = 'https://maoyan.com/board/4?'
        # https://maoyan.com/board/4?offset=40  0 10 20
    
    def get_html(self,url):
        headers = random.choice(useragents)
        req = urllib.request.Request(url)
        res = urllib.request.urlopen(req)
        html = res.read().decode()
        return html

    def save_html(self,filename,html):
        ab_file = '/home/tarena/正式课/爬虫/day01/maoyan/'+filename
        with open(ab_file,'wt') as f:
            f.write(html)
        
    def run(self):
        start = 1
        end = 10
        for page in range(1,11):
            offset = (page-1)*10
            canshu='offset=%s'%offset
            url = self.baseurl +canshu
            html = self.get_html(url)
            filename = '猫眼top100第%s页.html'%page
            self.save_html(filename,html)
            print('成功获取%s页'%page)
            time.sleep(5/10)

maoyan = Maoyan()
maoyan.run()