# coding:utf-8
import unittest,time
import requests
import re


class Login():
    def __init__(self, ses):  # 初始化
        self.s = ses

    def login(self, username="admin", psw="e10adc3949ba59abbe56e057f20f883e"):
        # s = requests.session()  # 不要在函数里面定义了，用形参s代替

        url = "http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html"

        h = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
            "Referer": "http://127.0.0.1/zentao/user-login.html",
            "Content-Type": "application/x-www-form-urlencoded",
            }

        body1 = {"account": username,
                "password": psw,
                "keepLogin[]":"on",
                "referer":"http://127.0.0.1/zentao/my/"
                }

        r1 = self.s.post(url, headers=h, data=body1)
        # print(r1.text)
        return r1.content.decode("utf-8")

    def fatie(self, s):
        self.s.post()
        print("发帖")




if __name__ == "__main__":
    s = requests.session()
    log = Login(s)  # 实例化的时候传参数
    log.login()  # 类去调用方法
