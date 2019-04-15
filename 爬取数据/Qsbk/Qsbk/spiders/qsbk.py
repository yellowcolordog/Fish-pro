# -*- coding: utf-8 -*-
import scrapy
from Qsbk.items import *
import datetime


class QsbkSpider(scrapy.Spider):
    name = 'qsbk'
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['http://www.qiushibaike.com/']

    def parse(self, response):

        # # 爬文字
        # url = aike.com/text/page/3/,
        # for i in range(2,3):
        #     url = self.start_urls[0]+'text/page/%s'%i
        #     yield scrapy.Request(url,callback=self.parse_text)
        
        # 爬图片
        # url = hibaike.com/imgrank/page/4/
        for i in range(1,4):
            url = self.start_urls[0] +'imgrank/page/%s'%i
            yield scrapy.Request(url,callback=self.parse_img)

    # 处理文字页面
    def parse_text(self,response):        
        contents = response.xpath('//div[@class="content"]/span/text()').extract()
        # 先去掉内容不全的文章：
        x = 0
        for i in contents:
            # print(type(i))
            if "查看全文" in i:
                contents.pop(x)
                contents.pop(x-1)
                x =x-2
            x+=1

        # 把文章内容发进管道
        for c in contents:
            item = QsbkItem() 
            item['text_content']=c
            yield item

    # 处理图片页面,得到图片数据
    def parse_img(self,response):
        contents = response.xpath('//div[@id="content-left"]/div')
        
        for c in contents:
            item = QsbkItem()

            ftime = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f') # 新设置图片文件名
            fname = ftime + '.' + 'jpg'
            item['img_name']=fname
            item['img_title'] = c.xpath('.//div[@class="content"]/span/text()')[0].extract().replace('\n','')            
            item['img_link'] = 'https:' + c.xpath('./div[@class="thumb"]//img/@src')[0].extract()
            
            yield item
