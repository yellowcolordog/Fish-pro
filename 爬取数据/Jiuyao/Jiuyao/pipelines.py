# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.files import FilesPipeline
import datetime
from .settings import *
import pymysql

class JiuyaoPipeline(object):
    def process_item(self, item, spider):
        fname = item['gif_name']
        print(item['gif_name'])
        fpath = GIF_PATH+fname # 得到图片路径,准备将图片信息保存进数据库,作为发帖数据

        # 建立mysql游标, 并指定数据库
        db = pymysql.connect(MYSQL_LOCATION,MYSQL_ACCOUNT,MYSQL_PASSWORD,db=MYSQL_DB,charset=MYSQL_CHARSET)
        cursor = db.cursor() 
        
        # 将数据存进mysql数据库
        ins1 = "insert into notes(create_date,note_raise,down,user_id) values(now(), 0,0,1);"
        ins2 = "insert into note_content(title,content,type,note_id) values('%s','%s',3,(select id from notes order by id DESC limit 1));"%(item['gif_title'],fpath)
        cursor.execute(ins1)
        db.commit()
        # print(ins2)
        cursor.execute(ins2)
        db.commit()

        return item


class JiuyaoImagePipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        # ftime = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
        # fname = ftime + '.' + 'gif'
        print(item['gif_title'])
        return scrapy.Request(item['gif_link'],meta=item)

    def file_path(self, request, response=None, info=None):  # 重写file_path 设置图片名字
        return request.meta['gif_name']
