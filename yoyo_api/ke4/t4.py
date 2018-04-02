# coding:utf-8

import requests

s = requests.session()  # 定义浏览器

loginUrl = "http://127.0.0.1/zentao/user-login.html"

h = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
}

body = {
    "account": "admin1",
    "password": "e10adc3949ba59abbe56e057f20f883e",
    "keepLogin[]": "on",
    "referer": "http://127.0.0.1/zentao/my/"
}

r1 = s.post(loginUrl, headers=h, data=body)
res = r1.content.decode("utf-8") # 解决乱码问题
print(res)
def is_login_sucess():
    if "登录失败，请检查您的用户名或密码是否填写正确" in res:
        print("登录失败！！！！！！！！！！")
        return False
    elif "parent.location='http://127.0.0.1/zentao/my/'" in res:
        print("登录成功！！！！！！！！！！！！！！！")
        return True
# print(is_login_sucess())

assert is_login_sucess()==True
# r2 = s.get("http://127.0.0.1/zentao/bug-view-25.html")
# print(r2.content.decode("utf-8"))

