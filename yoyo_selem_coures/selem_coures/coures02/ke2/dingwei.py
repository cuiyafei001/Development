# coding:utf-8
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
time.sleep(3)
driver.find_element_by_id("kw").send_keys(u"中文")   # unicode
time.sleep(3)
driver.find_element_by_id("su").click()  # 点击元素

# 清空输入框文本内容
time.sleep(3)
driver.find_element_by_id("kw").clear()  # 清空
time.sleep(4)
driver.find_element_by_id("kw").send_keys("hhhhh")


