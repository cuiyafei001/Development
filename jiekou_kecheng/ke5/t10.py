# coding:utf-8
import requests

s = requests.session()  # 可以当成微型浏览器
#
print(s.headers)
s.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0'

print(s.headers)  # 更新后的头部

token = "xxxx"
s.headers['token'] = token
print(s.headers)  # 更新后的头部

url = "http://www.cnblogs.com/yoyoketang/p/"

s.get(url)




