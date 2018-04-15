import time
import unittest

from selenium import webdriver

from yoyo_selem_coures.selem_coures.coures06.ke6.loginfuc import login

time.sleep(3)


class Liucheng():
    def di1bu(self):  # 方法，不叫函数
        print("第一步")

    def di2bu(self):
        print("第2步")


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.result = login(cls.driver) # 只登录一次

    def test_01(self): # 用例
        # 登录的功能
        print("登录之后，测试用例1")
        self.assertTrue(self.result == "admin")

    def test_02(self):    # 用例
        # login(self.driver)
        print("登录之后测试用例2")
        canshu = self.result
        print(canshu)

    def test_03(self):
        di1bu()
        di2bu()


if __name__ == "__main__":
    unittest.main()


if __name__ == "__main__":
    unittest.main()


