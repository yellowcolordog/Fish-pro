'''建库: AID1811db 建表: stuinfo'''

import pymysql

# 数据库连接对象
db = pymysql.connect('localhost','root','123456',charset='utf8')
# 游标对象(用来操作数据库)
cursor = db.cursor()
# 执行sql命令
c_db = 'create database if not exists AID1811db charset utf8'
u_db = 'use AID1811db'
c_tab = 'create table if not exists stuinfo(name varchar(20))'
ins = 'insert into stuinfo values("TOM")'
cursor.execute(c_db)
cursor.execulilte(u_db)
cursor.execute(c_tab)

cursor.execute(ins)
db.commit()
# 提交到数据库执行
cursor.close()
# 关闭
db.close()