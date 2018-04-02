# coding:utf-8
import requests
import unittest

class QQxjTestCase(unittest.TestCase):

    def setUp(self):
        self.url = "http://japi.juhe.cn/qqevaluate/qq"
        self.s = requests.session()

    def qq_xj(self, appkey, qq):  # 非test开头的叫方法
        par = {
              "key": appkey,  # appkey需要注册申请
              "qq":  qq
               }
        r = self.s.get(self.url, params=par)
        print(r.text)  # 打印文本
        result = r.json()  # 返回的是json,用r.json解析器转成字典
        # 字典取某个字段
        reason = result["reason"]
        print(reason)
        return reason

    def test_qq_01(self):  # test method names begin with 'test'
        result = self.qq_xj("8dbee1fcd8627fb6699bce7b986adc45", "11223344")
        self.assertTrue(result == "success")

    def test_qq_02(self):  # test method names begin with 'test'
        result = self.qq_xj(" ", "11223344")
        self.assertTrue(result == "KEY ERROR!")


if __name__ == '__main__':
    unittest.main()

