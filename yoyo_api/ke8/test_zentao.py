# coding:utf-8
import unittest,time
import requests
import re

url = "http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html"

h = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
"Referer": "http://127.0.0.1/zentao/user-login.html",
"Content-Type": "application/x-www-form-urlencoded",
}

body1 = {"account":"admin",
        "password":"e10adc3949ba59abbe56e057f20f883e",
        "keepLogin[]":"on",
        "referer":"http://127.0.0.1/zentao/my/"
        }

body2 = {"account":"admin111",
        "password":"e10adc3949ba59abbe56e057f20f883e",
        "keepLogin[]":"on",
        "referer":"http://127.0.0.1/zentao/my/"
        }

class TestLoginZenTao(unittest.TestCase):
    def setUp(self):
        self.s = requests.session()

    def test_login_pass(self):
        r = self.s.post(url, data=body1, headers=h)
        print(r.content)  # 打印结果看到location='http://127.0.0.1/zentao/my/'说明登录成功了
        result = re.findall(r"location='(.+?)';\n\n", r.text)   # 实际结果
        print(result[0])
        ex = "http://127.0.0.1/zentao/my/"
        self.assertEqual(result[0],ex)

    def test_login_fail(self):
        r = self.s.post(url, data=body2, headers=h)
        print(r.content)  # ('登录失败，请检查您的用户名或密码是否填写正确)
        print(type(r.content))
        import re
        result = re.findall(r"alert\('(.+?)'\)", r.content)   # 实际结果
        print(result[0])
        ex = "登录失败，请检查您的用户名或密码是否填写正确。"
        self.assertIn(ex, result[0])
        self.assertEqual(ex, result[0])

if __name__ == "__main__":
    unittest.main()

