# coding:utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("file:///C:/Users/Gloria/Desktop/alert.html")
time.sleep(1)
driver.find_element_by_id("prompt").click()
time.sleep(1)
# a = driver.switch_to_alert()

b = driver.switch_to_alert()

a = driver.switch_to.alert   # 后面是没括号的
a.send_keys("输入内容")
time.sleep(2)
a.accept()
# a.dismiss()

