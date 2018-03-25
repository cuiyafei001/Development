#!/usr/bin/env python

# -*- coding: UTF-8 -*-

import requests

url = "http://zzk.cnblogs.com/s/blogpost" # 问号前面的是URL地址

par = {
            "Keywords":"yoyoketang" # "":""这种格式为字典格式
      }   # par写问号后面的

h = {
            # "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
            "Cookie": "__utma=59123430.2039651162.1506178973.1506178973.1520166765.2; __utmz=59123430.1520166765.2.2.utmcsr=cnblogs.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _ga=GA1.2.2073439905.1507820943; _gid=GA1.2.1321958574.1520061142; __utmb=59123430.9.10.1520166765; __utmc=59123430; __utmt=1"
    }

r = requests.get(url,params=par,headers=h) # 写请求的参数类型

print(r.text)

