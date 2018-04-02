#!/usr/bin/env python

# -*- coding: UTF-8 -*-

a = [1, 2, 7, 12, 8, 9, 56]
print(len(a))  # len是一个函数查看长度

s = 0
for i in a:
    s += i
print(s)

# print(sum(a)) # sum是一个函数求和
print(sum(a))
