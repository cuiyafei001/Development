# coding:utf-8
import requests

s = requests.session()
# url = "http://xxxxxxx"
#
# body = {"user":"xxxx",
#         "psw":"xxxxxxxxxx"}
# r = s.post(url, data=body)
# # 返回的是json
# ret_token = r.json()["token"]
# print(ret_token)  # 打印出来看对不对

s.headers["token"] = "xxxxxxx"  # 在session里面管理头部
print(s.headers)


url2 = "http://http://www.cnblogs.com/yoyoketang/p/7004457.html"
# par = {"token": "%s" % ret_token}
# par = {"token": ret_token}
# h = {
#  "token": ret_token
#   }
body1 = {"key1": "value1",
         "key2": "value3",
         "token": "xxx"}
r2 = s.post(url2, json=body1)


