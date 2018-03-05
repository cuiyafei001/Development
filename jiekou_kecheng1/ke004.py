#!/usr/bin/env python

# -*- coding: UTF-8 -*-

import requests

url = "http://127.0.0.1/zentao/user-login.html"

body = {"account":"admin",
        "password":"e10adc3949ba59abbe56e057f20f883e",
        "keepLogin[]":"on",
        "referer":"http://127.0.0.1/zentao/my/"
        }

h = {"Content-Type": "application/x-www-form-urlencoded"}

# Content-Type: application/x-www-form-urlencoded 这种格式的body传data参数
r = requests.post(url,data=body,headers=h)

print(r.text)
print(r.content.decode("utf-8"))