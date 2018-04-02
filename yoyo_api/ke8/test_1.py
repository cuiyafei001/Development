# coding:utf-8
import unittest
import requests
from ke8.login_api import login

class Test_login(unittest.TestCase):

    def setUp(self):
        self.s = requests.session()

    def test_01(self):
        # 正确账号和正确密码
        result = login(self.s)
        print(result)
        self.assertIn("parent.location",result)

    def test_02(self):
        # 正确账号和正确密码
        result = login(self.s, "admin", "xxx")
        print(result)
        self.assertNotIn("parent.location",result)

