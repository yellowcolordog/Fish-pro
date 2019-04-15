
# -*- coding: utf-8 -*-
import scrapy
from Jiuyao.items import JiuyaoItem
import datetime

class JiuyaoSpider(scrapy.Spider):
    name = 'jiuyao'
    allowed_domains = ['www.9yao.com/gif']
    # start_urls = ['http://www.9yao.com/']

    def start_requests(self):
        for page in range(4,5):
            # 原网页格式: http://www.9yao.com/gif/index_2.html
            url = 'http://www.9yao.com/'+'/gif/index_%s.html'%page
            print(url) # http://www.9yao.com/gif/index_19.html
            yield scrapy.Request(url,callback=self.parse_one)

    # 2页开始的每个索引页,一级子界面
    def parse_one(self,response):
        # 得到每个索引也的response, 需要先用xpath解析每个gif块
        gifs = response.xpath('//div[@class="conBox"]')
        # print(gifs)
        for gif in gifs:
            # print(gif)
            # 得到每个gif块对象, 导入item,把信息放进item
            # gif_link = scrapy.Field() # gif路径
            # gif_name =  scrapy.Field() # gif名称
            # gif_title = scrapy.Field() # gif标题
            item = JiuyaoItem()
            item['gif_link'] = gif.xpath('./div[@class="videoPlayBox"]//img/@src').extract()[0]
            item['gif_title'] = gif.xpath('./h3/a/text()').extract()[0]
            ftime = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f') # 新设置图片文件名
            fname = ftime + '.' + 'gif'
            item['gif_name']=fname
            # print(item)
            yield item