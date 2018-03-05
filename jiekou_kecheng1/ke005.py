#!/usr/bin/env python

# -*- coding: UTF-8 -*-

import requests

url = "http://127.0.0.1/zentao/user-login.html"

body = {"account":"xxx",
        "password":"111"
        }

h = {"Content-Type": "application/x-www-form-urlencoded"}

# Content-Type: application/json 这种格式的body传json参数
r = requests.post(url,json=body,headres=h)

print(r.text)