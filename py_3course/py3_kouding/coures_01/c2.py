#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import random
import math
# number = input("随便输入一个整数")
# print(help(math))
#
# print(2/3)
# print(abs(12))
# print(math.pi)
# num = int(input("请输入一个整数！！！"))
#
# if num % 2 == 0:
#     print("这个是偶数！")
# else:
#     print("这个是基数！")
'''
打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，
其各位数字立方和等于该数本身。例如：153是一个“水仙花数”，
因为153=1的三次方＋5的三次方＋3的三次方。
'''
# print(math.floor(1.8))
# math.floor（x ）将x的底部作为浮点数返回，最大的整数值小于或等于x。
for i in range(100, 1000):
    x = math.floor(i/100)  # 先获取百位数
    # print(x)
    y = math.floor((i - x*100)/10)  # 获取十位数
    # print(y)
    z = i - math.floor(i/10)*10     # 回去个位数
    # print(z)
    if i == x**3 + y**3 + z**3:
        print(i, end=',')
