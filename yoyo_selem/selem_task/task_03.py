#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
web自动化作业
笔试题1: 仙花数是指一个 n 位数 ( n≥3 ),
它的每个位上的数字的 n 次幂之和等于它本身.
（例如：1^3 + 5^3 + 3^3 = 153），用Python算出100-1000的所有水仙花数，打印出来
"""
import random

for i in range(100, 1000):
    x = i % 10           # 取个位数
    y = i // 10 % 10     # 取十位数
    z = i // 100         # 取百位数
    if x ** 3 + y ** 3 + z ** 3 == i:
        # end 默认是"\n"
        # print(i)
        print(i, end='，')

'''
如何交换a和b的值？
打印a=2,b=1
'''
a = 1
b = 2
a, b = b, a
print(a, b)

'''
用python写一个猜数字的游戏，游戏规则如下：
1.由一个人随机写一个整数1-99（如：21）
2.一群小伙伴轮流猜数字，如第一个人猜一个数（如：48），
则缩小范围为（1-48）
3.如第二个人猜一个数（如：9），则缩小范围为（9-48）
4.以此类推，值到猜中数字（21），游戏结束
'''
number = random.randint(1, 99)
num = int(input("请输入一个整数1到99："))

while True:
    if num == number:
        print("猜对了！！！")
    elif num > number:
        print("")
