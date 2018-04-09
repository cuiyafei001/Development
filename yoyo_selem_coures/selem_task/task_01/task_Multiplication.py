#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
# 打印99乘法口诀
"""
print("99乘法口诀表：")

for i in range(1, 10):
    for j in range(1, 10):
        if i >= j:
            print("%d * %d = %2d " % (i, j, i*j), end=" ")
    print(" ")
