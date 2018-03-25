#!/usr/bin/env python

# -*- coding: UTF-8 -*-

# 列表用方括号表示[]
bicycles = ['trek','cannondale','redline','specialized']
# list[] 索引是从0开始的
print(bicycles[0].upper())
print(bicycles[1].title())
print(bicycles[2].lower())
# python访问list[]最后一个索引可为-1
print(bicycles[-1])
# python访问list[]倒数第二个个索引可为-2
print(bicycles[-2])

# 去list中的值创建消息
message = "My first bicycles a " + bicycles[0].title() + "."
print(message)
