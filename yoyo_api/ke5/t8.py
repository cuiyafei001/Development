# coding:utf-8
from urllib import parse

a = "中文"
print(parse.quote(a))

b = parse.quote(a)

url = "http://zzk.cnblogs.com/s/blogpost?Keywords=%s" % b
print(url)
