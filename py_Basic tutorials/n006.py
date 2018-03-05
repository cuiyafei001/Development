#!/usr/bin/env python

# -*- coding: UTF-8 -*-

import pymysql.cursors
pymysql.install_as_MySQLdb()

# 连接MySQL数据库
connect = pymysql.Connect(
    host = 'localhost',
    port = '3306',
    user = 'root',
    password = 'csliyi001',
    db = 'python',
    charset = 'utf-8'
)

# 创建游标
cursor = connect.cursor(cursor=pymysql.cursors.DictCursor)

# 执行语句返回影响的行数
effect_row = cursor.execute("select * from course")
print(effect_row)
# 获取所有数据
result = cursor.fetchall()
result1 = cursor.fetchone()  # 获取下一个数据
result2 = cursor.fetchone()  # 获取下一个数据（在上一个的基础之上）
# cursor.scroll(-1, mode='relative') # 相对位置移动
# cursor.scroll(0,mode='absolute') # 绝对位置移动

# 提交，不然无法保存新建或者修改的数据
connect.commit()
# 关闭游标
cursor.close()
# 关闭连接
connect.close()

