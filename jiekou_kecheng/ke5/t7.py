# coding:utf-8
import requests
from urllib import parse
url = "http://zzk.cnblogs.com/s/blogpost?Keywords=中文"
r = requests.get(url)

print(r.url)  # 返回的url
res = r.url

# 对整个url解码
print(parse.unquote(res))


res1 = res.split("?")[1]
res2 = res1.split("&")
print(res2)

for i in res2:
    if "Keywords" in i:
        print(i.split("=")[1])
        a = i.split("=")[1]


b = "%E4%B8%AD%E6%96%87"
c = parse.unquote(b)
print(c)









