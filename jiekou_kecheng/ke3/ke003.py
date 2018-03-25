#!/usr/bin/env python

# -*- coding: UTF-8 -*-

import requests

url = "https://www.baidu.com/"
r = requests.get(url)
# print(r.text) # 文本格式打印会有乱码
# 字节方式输出
# 有乱码就加这个
print(r.content.decode("utf-8"))
print(r.encoding) # 返回页面的编码格式
print(r.url)      # 查看返回的URL
print(r.status_code) # 查看返回的状态码

print(r.raw)

