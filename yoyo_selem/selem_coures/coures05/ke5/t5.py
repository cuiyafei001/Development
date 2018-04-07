# coding:utf-8
import unittest
from selenium import webdriver
import time

class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    def setUp(self):
        self.driver.get("http://127.0.0.1/zentao/user-login.html")
        time.sleep(3)

    # def setUp(self):
    #     self.driver = webdriver.Firefox()
    #     self.driver.get("http://127.0.0.1/zentao/user-login.html")
    #     time.sleep(3)

    def test_01(self):
        self.driver.find_element_by_id("account").send_keys("admin")
        self.driver.find_element_by_name("password").send_keys("1111111")
        # self.driver.find_element_by_id("submit").click()
        time.sleep(3)  # 页面跳转地方sleep下

        # t = self.driver.find_element_by_css_selector("#userMenu>a").text  # 未登录成功！！
        # print(t)  # 实际结果
        # self.assertTrue("admin" != t)
        # self.assertEqual("admin", t)

    def test_02(self):
        self.driver.find_element_by_id("account").send_keys("admin")
        self.driver.find_element_by_name("password").send_keys("123456")
        self.driver.find_element_by_id("submit").click()

        time.sleep(3)  # 页面跳转地方sleep下
        t = self.driver.find_element_by_css_selector("#userMenu>a").text
        print(t)  # 实际结果
        self.assertTrue("admin" == t)
        # self.assertEqual("admin", t)

    def test_03(self):
        self.driver.find_element_by_id("account").send_keys("admin")
        self.driver.find_element_by_name("password").send_keys("123456")
        self.driver.find_element_by_id("submit").click()

        time.sleep(3)  # 页面跳转地方sleep下
        t = self.driver.find_element_by_css_selector("#userMenu>a").text
        print(t)  # 实际结果
        self.assertTrue("admin" == t)
        # self.assertEqual("admin", t)


    def tearDown(self):
        self.driver.delete_all_cookies() # 退出登录
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
         cls.driver.quit()

    # def tearDown(self):
    #     self.driver.quit()

if __name__ == "__main__":
    unittest.main()



