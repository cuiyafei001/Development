# coding:utf-8
import requests
import unittest

class QQxjTestCase(unittest.TestCase):

    def setUp(self):
        self.url = "http://japi.juhe.cn/qqevaluate/qq"
        self.s = requests.session()

    def test_qq_01(self):  # test method names begin with 'test'
        # 这个key参数是我个人申请的，所以本群内部使用就行了，希望大家别乱发
        par = {
              "key": "8dbee1fcd8627fb6699bce7b986adc45",  # appkey需要注册申请
              "qq":  "283340479"
               }
        r = self.s.get(self.url, params=par)
        print(r.text)  # 打印文本
        result = r.json()  # 返回的是json,用r.json解析器转成字典
        # 字典取某个字段
        reason = result["reason"]
        print(reason)
        self.assertTrue(reason == "success")


    def test_qq_02(self):  # test method names begin with 'test'
        # 这个key参数是我个人申请的，所以本群内部使用就行了，希望大家别乱发
        par = {
              "key": " ",  # appkey需要注册申请
              "qq":  "283340479"
               }
        r = self.s.get(self.url, params=par)
        print(r.text)  # 打印文本
        result = r.json()  # 返回的是json,用r.json解析器转成字典
        # 字典取某个字段
        reason = result["reason"]
        print(reason)
        self.assertTrue(reason == "KEY ERROR!")


if __name__ == '__main__':
    unittest.main()

