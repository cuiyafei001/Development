#!/usr/bin/env python

# -*- coding: UTF-8 -*-

import requests

# 第一个python 3.6 的接口请求
url = "http://www.cnblogs.com/cyfyywfc/"
h = {  }   # 头部暂时不写
r = requests.get(url)

print(r.status_code) # 打印状态码
print(r.headers)     # 打印头部信息
print(r.text)        # 打印正文