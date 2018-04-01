#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########## prepare ##########

import pymysql
 
# 打开数据库连接
db = pymysql.connect("localhost","root","root","test" )
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
# 使用 execute()  方法执行 SQL 查询 
# cursor.execute("SELECT * form admin where admin_id=1")
cursor.execute("SELECT VERSION()")
 
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
 
print ("Database version : %s " % data)
 
# 关闭数据库连接
db.close()