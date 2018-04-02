# coding:utf-8
import requests


# 登录之后，获取token返回之后的token

token = "Xxxxxxxx"
# token放在三个部分head、params、body里面
h = {
    "token": token
}

url = "http://www.xxx.com"
par = {
    "token": token
}

body = {
    "token": token
}

c = "cookies参数"

r = requests.post(url, headers=h, params=par, data=body, cookies=c)
