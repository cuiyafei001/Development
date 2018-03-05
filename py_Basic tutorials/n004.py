#!/usr/bin/env python

# -*- coding: UTF-8 -*-

# 如何读取键盘输入
__author__ = "池塘的落叶"

if __name__ == "__main__":
    # 读取键盘任意输入

    data = input("请输入任意一个字符")

    # 以空格切割输入的字符串
    list_data = data.split( ' ')

    # 打印切割后的列表数据
    print(list_data)
