# coding:utf-8
from selenium import webdriver
import unittest
from yoyo_selem_coures.selem_coures.coures07.ke7.loginpage import LoginPage


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 类方法
        cls.driver = webdriver.Firefox()

    def setUp(self):
        # 实例方法
        self.driver = webdriver.Firefox()
        self.loginpage = LoginPage(self.driver)

    def ffa(self):
        print("heee")

    @staticmethod
    def jingtaide():  # 静态方法
        print("hello world")

    def test_01(self):
        res = self.loginpage.login()  # 登录
        print(res)  # 获取登录结果
        # 断言
        self.assertTrue("admin" == res)

    def tearDown(self):
        self.loginpage.logout()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()