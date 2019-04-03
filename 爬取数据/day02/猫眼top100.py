import urllib.request
import urllib.parse
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


class Maoyan:
    def __init__(self):
        self.baseurl = 'https://maoyan.com/board/4?'
        # https://maoyan.com/board/4?offset=40  0 10 20
    
    def get_html(self,url):
        headers = random.choice(useragents)
        print(headers)
        req = urllib.request.Request(url)
        res = urllib.request.urlopen(req)
        html = res.read().decode()
        return html

    def save_html(self,filename,html):
        ab_file = '/home/tarena/正式课/爬虫/day02/maoyan/'+filename
            # <dd>
            #                         <i class="board-index board-index-1">1</i>
            #     <a href="/films/1203" title="霸王别姬" class="image-link" data-act="boarditem-click" data-val="{movieId:1203}">
            #       <img src="//s0.meituan.net/bs/?f=myfe/mywww:/image/loading_2.e3d934bf.png" alt="" class="poster-default">
            #       <img data-src="https://p1.meituan.net/movie/20803f59291c47e1e116c11963ce019e68711.jpg@160w_220h_1e_1c" alt="霸王别姬" class="board-img">
            #     </a>
            #     <div class="board-item-main">
            #       <div class="board-item-content">
            #               <div class="movie-item-info">
            #         <p class="name"><a href="/films/1203" title="霸王别姬" data-act="boarditem-click" data-val="{movieId:1203}">霸王别姬</a></p>
            #         <p class="star">
            #                 主演：张国荣,张丰毅,巩俐
            #         </p>
            # <p class="releasetime">上映时间：1993-01-01</p>    </div>
            #     <div class="movie-item-number score-num">
            # <p class="score"><i class="integer">9.</i><i class="fraction">5</i></p>        
            #     </div>

            #       </div>
            #     </div>
            #                 </dd>
        p = re.compile(r'<dd>.*?title="(.*?)" class="image-link".*?<p class="star">\s*?(.*?)\s*</p>.*?class="releasetime">(.*?)</p>',re.S)
        L = p.findall(html)

        with open(ab_file,'a') as f:
            writer = csv.writer(f)
            for t in L:
                writer.writerow(t)

    def run(self):
        start = 1
        end = 10
        for page in range(1,11):
            offset = (page-1)*10
            canshu='offset=%s'%offset
            url = self.baseurl +canshu
            html = self.get_html(url)
            filename = '猫眼top100第%s页.csv'%page
            self.save_html(filename,html)
            print('成功获取%s页'%page)
            time.sleep(5/10)

maoyan = Maoyan()
maoyan.run()r'<dd>.*?title="(.*?)" class="image-link".*?<p class="star">\s*?(.*?)\s*</p>.*?class="releasetime">(.*?)</p>'