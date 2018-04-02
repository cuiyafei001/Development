# coding:utf-8

import requests

url = "http://japi.juhe.cn/qqevaluate/qq"


# 这个key参数是我个人申请的，所以本群内部使用就行了，希望大家别乱发
par = {
      "key": "8dbee1fcd8627fb6699bce7b986adc45",  # appkey需要注册申请
      "qq":  "283340479"
       }

r = requests.get(url, params=par)
print(r.text)  # 打印文本
result = r.json()  # 返回的是json,用r.json解析器转成字典

# 字典取某个字段
reason = result["reason"]
print(reason)