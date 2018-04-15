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
        # 第一步：登录
        self.loginpage.login("admin", "123456")
        # 第二步：获取结果
        res = self.loginpage.get_login_result()
        # 第三步：断言
        # 断言
        self.assertTrue("admin" == res)

    def tearDown(self):
        self.loginpage.logout()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
