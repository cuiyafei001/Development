#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
web自动化作业
课前作业:1.安装好pycharm，在pycharm里面写脚本成功启动火狐浏览器， 截图提交
"""

from selenium import webdriver
import time

driver = webdriver.Ie()
url = "https://www.baidu.com/"
driver.get(url)
time.sleep(3)
# driver.quit()
