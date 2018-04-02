#!/usr/bin/env python

# -*- coding: UTF-8 -*-

import datetime

# 获取系统当前日期时间
now_time = datetime.datetime.now()
print(now_time)

# python 一行代码打印乘法口诀
print ('\n'.join([' '.join(['%s*%s=%-2s' % (y,x,x*y) for y in range(1,x+1)]) for x in range(1,10)]))



