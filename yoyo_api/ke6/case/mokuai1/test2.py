# coding:utf-8
import requests
import unittest

class TestQQXJ(unittest.TestCase):
    def test_1(self):
        url = "http://japi.juhe.cn/qqevaluate/qq"

        par = {
            "key": "8dbee1fcd8627fb6699bce7b986adc45",
            "qq": "283340479"
        }
        r1 = requests.get(url, params=par)
        print(r1.text)  # json数据
        # 最简单的转字典方法
        res = r1.json()  # json解析器，自动转字典
        print(res["reason"])
        print(res['result']['data']['conclusion'])
        print(res['result']['data']['analysis'])