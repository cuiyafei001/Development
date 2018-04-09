#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("所有用例执行前只执行一次！！！")

    @classmethod
    def tearDownClass(cls):
        print("所有用例执行完执行一次！！！")

    # def login(self):
    #     print("执行测试用例前先登录！！！")
    #
    # def logout(self):
    #     print("执行完测试用例退出登录")

    def setUp(self):
        # 在每个测试用例之前都会执行一次
        print("这是测试的前置条件!!!")
        # self.login()

    def tearDown(self):
        # 在每个测试用例之后都会执行一次
        print("这是测试用例的后置条件!!!")
        # self.logout()

    def test_001(self):
        print("测试用例11111111111111111")

    def test_002(self):
        print("测试用例22222222222222222")

    def test_003(self):
        print("测试用例33333333333333333")

    def test_004(self):
        print("测试用例44444444444444444")

    def test_005(self):
        print("测试用例55555555555555555")


if __name__ == "__main__":
    unittest.main()
