#!/usr/bin/env python
# -*- coding:utf-8 -*-

# \n 代表回车键 转义字符 换行
print("hello world!!!")

# 转义字符 \
# \n是回车键
print("hello\nworld")
# \\双反斜杠代表不转义
print("hello\\nworld")
# raw是原型  不转义
print(r"hello\nworld")

# 连接符
a = "hello"
b = "world"
print(a + b)

# 格式化输出
name = "Harvey"
age = 18
print("My name is : " + name)
print("My name is : " + name + " is My name")
# %参数化占位符
print("My name is : %s haohaohao" % name)

# 多个参数用，隔开
print("My name is: %s, age is: %s" % (name, age))

# 强制转换类型
print(name + str(age))
