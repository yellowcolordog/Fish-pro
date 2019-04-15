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
        # # url = aike.com/text/page/3/,
        # for i in range(2,5):
        #     url = self.start_urls[0]+'text/page/%s'%i
        #     yield scrapy.Request(url,callback=self.parse_text)
        
        # 爬图片
        # url = hibaike.com/imgrank/page/4/
        for i in range(1,4):
            url = self.start_urls[0] +'imgrank/page/%s'%i
            yield scrapy.Request(url,callback=self.parse_img)

    # 处理文字页面
    def parse_text(self,response):        
        # print(2)
        hrefs = response.xpath('//div[@id="content-left"]/div/a[@class="contentHerf"]/@href').extract()
        # https://www.qiushibaike.com/article/121686485
        for href in hrefs:
            url = 'https://www.qiushibaike.com' + href
            # print(url)
            # 将文字页面再交给二级页面处理(避免一些文章不展开全文的问题)
            yield scrapy.Request(url,callback=self.parse_text2)

    # https://www.qiushibaike.com/article/121686485  处理单独文字页面,得到文字数据
    def parse_text2(self,response):

        item = QsbkItem()
        item['text_title']=response.xpath('//h1[@class="article-title"]/text()')[0].extract()
        word = response.xpath('//div[@class="content"]/text()')[0].extract()
        item['text_content'] = word.replace('<br>','\n')
        # print(item['text_content'])
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
