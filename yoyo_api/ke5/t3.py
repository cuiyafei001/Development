# coding:utf-8
import requests
import json
# post请求，content-type:application/json

url = "http://www.xxx.com/x"
h = {
    "content-type": "application/json"
}
body = {
    "key1": "value1",
    "key2": "value2",
}
# r1 = requests.post(url, json=body, headers=h)  # 前面讲的第一种方法

# 用data参数传json格式的数据
# r2 = requests.post(url, data=json.dumps(body), headers=h)

