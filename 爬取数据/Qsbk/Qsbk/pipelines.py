# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from .settings import *
import scrapy
import pymysql
from scrapy.pipelines.files import FilesPipeline

class QsbkPipeline(object):
    def process_item(self, item, spider):
        # 建立mysql游标, 并指定数据库
        db = pymysql.connect(MYSQL_LOCATION,MYSQL_ACCOUNT,MYSQL_PASSWORD,db=MYSQL_DB,charset=MYSQL_CHARSET)
        cursor = db.cursor() 
        
        # 将文字数据存进mysql数据库
        if 'text_content' in item:
            ins1 = "insert into notes(create_date,note_raise,down,user_id) values(now(), 0,0,1);"
            ins2 = "insert into note_content(title,content,type,note_id) values('%s','%s',1,(select id from notes order by id DESC limit 1));"%('搞笑段子',item['text_content'])
            cursor.execute(ins1)
            db.commit()
            cursor.execute(ins2)
            db.commit()
            print(1)
         
        # 将图片数据存进mysql数据库
        elif 'img_name' in item:
            fpath = IMG_PATH+item['img_name']
            ins1 = "insert into notes(create_date,note_raise,down,user_id) values(now(), 0,0,1);"
            ins2 = "insert into note_content(title,content,type,note_id) values(\
                '%s','%s',2,(select id from notes order by id DESC limit 1));"%(item['img_title'],fpath)
            # print(item['img_title'],fpath)
            cursor.execute(ins1)
            db.commit() 
            cursor.execute(ins2)
            db.commit()
            

        return item

# 将图片保存到本地
class QsbkImgPipline(FilesPipeline):
    def get_media_requests(self,item,info):
        print(item['img_title'])
        return scrapy.Request(item['img_link'],meta=item)

    def file_path(self, request, response=None, info=None):
        return request.meta['img_name']