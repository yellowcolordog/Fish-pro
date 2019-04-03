import csv
import requests
import re

href=r'<a href="(.*?)/.*?</a>'

class NoteSpider(object):
    def __init__(self):
        self.headers={'User-Agent':"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0"}
        self.proxies={'http':'http://309435365:szayclhp@116.255.191.105:16816'}
        self.auth = ('tarenacode','code_2013')
        self.baseurl = "http://code.tarena.com.cn/"
    # 获取解析页面
    def get_page(self,url):
        res = requests.get(url,headers=self.headers,proxies=self.proxies,auth=self.auth)
        res.encoding='utf-8'
        html = res.text
        p = re.compile(r'<a href="(.*?)/.*?</a>',re.S)
        l = p.findall(html)
        self.write_page(l)
    
    # 保存数据
    def write_page(self,r_list):
        with open('note.csv','w') as f:
            writer = csv.writer(f)
            for r in r_list[1:]:
                writer.writerow([r])
                print('成功写入')

if __name__ =='__main__':
    spider = NoteSpider()
    spider.get_page("http://code.tarena.com.cn/")