# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JiuyaoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    gif_link = scrapy.Field() # gif路径
    gif_name =  scrapy.Field() # gif名称
    gif_title = scrapy.Field() # gif标题