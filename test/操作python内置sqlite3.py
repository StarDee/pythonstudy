# !urs/bin/env python
# -*- utf:8 -*-
#导入SQLite驱动
import sqlite3
# 连接到SQlite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建
conn=sqlite3.connect('test.db')
#创建一个cursor
cursor=conn.cursor()
#执行一条SQL语句，创建user表
cursor.execute('create table user (id varchar(20) primary key,name varchar(20))')


# 通过rowcount获得插入的行数
cursor.rowcount
#关闭cursor
cursor.close()
#提交事物
conn.commit()
#关闭connection
conn.close()