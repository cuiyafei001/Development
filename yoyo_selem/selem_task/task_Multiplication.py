#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
# 打印99乘法口诀
"""
for i in range(1, 10):
    for j in range(1, 10):
        if i >= j:
            print("%s * %s = %s " % (i, j, i*j), end=" ")
    print(" ")
