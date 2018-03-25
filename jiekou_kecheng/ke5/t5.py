# coding:utf-8
import requests
url = "http://japi.juhe.cn/qqevaluate/qq"

par = {
    "key": "8dbee1fcd8627fb6699bce7b986adc45",
    "qq": "283340479"
}

r1 = requests.get(url, params=par)
print(r1.text)  # json数据

result = r1.text
print(type(result))

# 通过json模块去转
import json
print(json.loads(result))
print(type(json.loads(result)))

# 最简单的转字典方法
res = r1.json()  # json解析器，自动转字典
print(type(res))
print(res)

print(res['reason'])
# 通过key值查找，多个目录就找到父元素
print(res['result']['data']['conclusion'])
print(res['result']['data']['analysis'])

