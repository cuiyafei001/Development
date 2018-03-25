# # coding:utf-8

import requests
import urllib3
urllib3.disable_warnings()


s1 = requests.session()  # 谷歌
s2 = requests.session()  # Firefox

s1.get("https://www.baidu.com")

s2.get("http://www.cnblogs.com/yoyoketang/p/")

s1.post()

s2.post()

