# coding:utf-8
import unittest
from selenium import webdriver
import time
import unittest


# 参数化
def login(driver,usrname="admin", psw="123456"):  # 这里的driver是形参
    '''登录函数'''
    # 保证函数里面的每个参数都要定义
    driver.get("http://127.0.0.1/zentao/user-login.html")
    time.sleep(3)
    # 登录
    driver.find_element_by_id("account").send_keys(usrname)
    driver.find_element_by_name("password").send_keys(psw)
    driver.find_element_by_id("submit").click()


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_01(self):
        login(self.driver)


if __name__ == "__main__":
    unittest.main()




