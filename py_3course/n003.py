#!/usr/bin/env python

# -*- coding: UTF-8 -*-

# Python3 编程第一步
# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
# a,b = 0,1
# while b < 10:
#     print(b)
#     a,b = b,a + b
#
# i = 256 * 256
# print('i的值为：', i)

# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
# s,x = 0,1
# while x < 1000:
#     print(x,end = ',')
#     s,x = x,s + x

# if语句
a = 10
if a :
    print("1 - if 表达式条件为 true")
    print(a)
b = 0
if b :
    print("2 - if 表达式条件为 true")
    print(b)
print("Good bay!!!")

# 判断年龄
age = int(input("请输入你家猫猫的年龄:"))
print("")
if age < 0:
    print("小子,你在逗我吗")
elif age == 1:
    print("相当于 10 岁的人：")
elif age == 2:
    print("相当于 20 岁的人：")
elif age > 2:
    print("相当于 99 岁的人：")

### 退出提示
print("点击 enter 建退出 ！")
