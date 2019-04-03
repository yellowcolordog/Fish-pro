from urllib import request
from urllib import parse
import random
import time 
import re
import csv

useragents = [
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'},
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'},
    {'User-Agent':'Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50'},
    {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; ) AppleWebKit/534.12 (KHTML, like Gecko) Maxthon/3.0 Safari/534.12'},
    {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.33 Safari/534.3 SE 2.X MetaSr 1.0'},
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 QQBrowser/6.9.11079.201'},
]

class MaoyanSpider(object):
    def __init__(self):
        self.baseurl = 'https://maoyan.com/board/4'


    def get_page(self,url):
        headers = random.choice(useragents)
        req = request.Request(url,headers=headers)
        res = request.urlopen(req)
        html = res.read().decode()
        data = self.parse_page(html)
    
    def parse_page(self,html):
        p = re.compile(r'<dd>.*?title="(.*?)" class="image-link".*?<p class="star">\s*?(.*?)\s*</p>.*?class="releasetime">(.*?)</p>',re.S)
        r_list = p.findall(html)
        # r_list:[('霸王别姬','张国荣',1993-1-1),('勇敢的心','入野自由','1992-1-1')...]
        self.write_csv(r_list)

    def write_csv(self,r_list):
        filename = 'maoyan/猫眼电影第%s页.csv'%self.page
        with open(filename,'a') as f:
            writer = csv.writer(f)
            for r_t in r_list:
                writer.writerow(r_t)
            
    def work_on(self):
        for page in range(1,11):
            self.page = page
            pn = str((page-1)*10)
            url = self.baseurl+'?offset=%s'%pn
            self.get_page(url)
            time.sleep(2)
            print('成功获取%s页'%page)


if __name__ =='__main__':
    begin = time.time()
    spider = MaoyanSpider()
    spider.work_on()
    end = time.time()
    print('执行时间:%.2f'%(end-begin))