# coding:utf-8
import unittest
# 前置和后置
import time

class Test1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("所有用例执行之前先执行这里：-------setUpClass")

    # def setUp(self):
    #     print("每个用例执行之前先执行这里：-------setUp")

    # def tearDown(self):
    #     print("每个用例执行之后再执行这里：-------tearDown")
    #     time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        print("所有用例执行之后执行这里：-------tearDownClass")

    def test_01(self):
        print("测试用例01----------01")
        time.sleep(1)

    def test_02(self):
        print("测试用例02----------02")
        time.sleep(1)

if __name__ == "__main__":
    unittest.main()

