from random import choice
import requests
import pymysql
from time import sleep
import re
import datetime
useragents = [
    # {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'},
    # {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},
    # {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'},
    # {'User-Agent':'Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50'},
    # {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; ) AppleWebKit/534.12 (KHTML, like Gecko) Maxthon/3.0 Safari/534.12'},
    # {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.33 Safari/534.3 SE 2.X MetaSr 1.0'},
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 QQBrowser/6.9.11079.201'},
]

class GifSpider(object):
    def __init__(self):
        self.baseurl = 'http://www.gaoxiaogif.cn/baoxiaogif/'
        # http://www.gaoxiaogif.cn/baoxiaogif/1-7.html
        self.db = pymysql.connect('localhost','root','123456',charset='utf8')
        self.cursor = self.db.cursor()

    def get_html(self,url):
        headers = choice(useragents)
        res = requests.get(url,headers=headers)
        res.encoding = 'utf-8'
        return res.text

    def save_gif(self,html):
        p = re.compile('class="block">.*?target="_ablank"\s?>(.*?)</a></h2>.*?<img.*?(http:.*?)\'? alt=',re.S)
            #  >坐摩托穿裙子有多飘逸？下图告诉你！                                            ……</a></h2>\r\n      <div class="clear"></div>\r\n      \r\n      <div class=\'viewimg\'> <a href=\'/./gif-411.html\' title=\'穿裙子坐摩托的gif动态图片_搞笑gif_搞笑gif动态图\' target=\'_ablank\' class=\'ipic\'> <img src=\'http://img.gaoxiaogif.cn/GaoxiaoGiffiles/images/2015/06/15/chuanqunzizuomotuo.gif\' 
        l = p.findall(html)
        i=1
        for t in l:
            title = t[0].replace(' ','') # 图片简介
            src = t[1] # 图片网址
            filepath = self.save_img(src) # 图片本地路径
            data = (title,src,filepath)
            ins = 'insert into gaoxiaogif(title,src,filepath)values("%s","%s","%s");'%data
            self.cursor.execute(ins)
            self.db.commit()
            print('爬取成功%s'%i)
            i += 1


    def save_img(self,url):
        headers = choice(useragents)
        res = requests.get(url,headers=headers)
        img = res.content # 获取img二进制数据

        ftime = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
        fname = ftime + '.' + url.split('.')[-1] # 造出文件名
        filepath = '/home/tarena/正式课/tarena_program/爬取数据/gaoxiaogif/gif/'+fname
        with open(filepath,'wb') as f: # 将图片保存进服务器
            f.write(img)
        return filepath #返回保存路径

    def work_on(self):
        self.cursor.execute('use gifspider')
        for page in range(1,8):
            url = self.baseurl +'%s.html'%page
            html = self.get_html(url)
            self.save_gif(html)
        self.cursor.close()
        self.db.close()

gaoxiaogif = GifSpider()
gaoxiaogif.work_on()

