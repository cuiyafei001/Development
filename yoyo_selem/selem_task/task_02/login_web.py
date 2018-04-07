#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
web自动化作业悠悠我心 昨天 星期日 12:11
第2课作业：
1.随便找个你们自己公司的网站（没有验证码的那种）
输入账号、密码。点登录，能登录成功
2.登录成功后，代码截图提交
"""
from selenium import webdriver
import time


def Login(user, paw):
    u'''登录'''
    driver.get("http://192.123.1.123:8080/login/")
    time.sleep(1)
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("password").clear()
    time.sleep(2)
    driver.find_element_by_id("username").send_keys(user)
    driver.find_element_by_id("password").send_keys(paw)
    time.sleep(2)
    driver.find_element_by_xpath(".//*[@id='loginbox']/div/div[2]/form/div[4]/div/div/input").click()
    return driver


if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver = Login("XXX", "XXX")

    t = driver.find_element_by_xpath("html/body/div[1]/div[2]/h3").text
    # 在不确定title的情况下可以先打印出来看下
    print(t)
    if t == "欢迎！":
        print("登录成功")
    else:
        print("登录失败")
