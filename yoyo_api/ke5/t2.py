# coding:utf-8
import json

d = {
    "a": 111,
    "b": "1222",
    "c": True,
    "d": ["a","b"],
    "e": 122.3,
    "f": False,
    "g": None}
print(type(d))
print(d)
print(str(d))

# 字典转json
print("-----字典转json-----------")
d_json = json.dumps(d)
print(d_json)
print(type(d_json))

# json转字典
j_dict = json.loads(d_json)
print(j_dict)

