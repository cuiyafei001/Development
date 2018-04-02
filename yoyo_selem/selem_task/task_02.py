#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
web自动化作业悠悠我心 昨天 星期日 08:59
笔试题2:
用Python写一个冒泡排序，注意打印出排序过程中数据交换过程
"""

lis = [12, 4, 66, 78, 11, 6, 88, 45, 29]
print("初始化list：%s" % lis)
num = len(lis)
s = 1
while 1:
    for i in range(num-s):
        if lis[i] > lis[i+1]:
            temp = lis[i]
            lis[i] = lis[i+1]
            lis[i+1] = temp
    s += 1
    print("每次list的排序变化：%s" % lis)
    if s == num - 1:
        break
print("list最终排序结果：%s" % lis)

