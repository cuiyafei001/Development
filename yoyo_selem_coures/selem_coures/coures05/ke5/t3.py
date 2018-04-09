# coding:utf-8
import unittest
from ke5.loginout import *

class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("所有的用例之前，只执行一次")

    @classmethod
    def tearDownClass(cls):
        print("所有的用例之后，只执行一次")

    # def tearDown(self):
    #     # 在每个测试用例之后都会执行一次
    #     print("这个是测试的后置操作！")
    #     logout()
    #
    # def setUp(self):
    #     # 在每个测试用例之前都会执行一次
    #     print("这个是测试的前置操作!")
    #     login()

    def test_A11(self):
        print("测试用例A11A11A11A11")

    def test_aaaa(self):
        print("测试用例aaaaaaaaaaaa")

    def test_7777(self):
        print("测试用例7777")

if __name__ == "__main__":
    unittest.main()