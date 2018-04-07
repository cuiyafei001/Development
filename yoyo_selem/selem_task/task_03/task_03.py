#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
第3课作业:
1.百度搜索设置-设置每页显示条数，点保存设置，
弹出alert，打印出alert内容和点确定按钮。代码截图提交
"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
time.sleep(3)
s = driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(s).perform()
time.sleep(0.5)
driver.find_element_by_link_text("搜索设置").click()
time.sleep(1)
driver.find_element_by_xpath(".//*[@id='nr']/option[3]").click()
driver.find_element_by_xpath(".//*[@id='gxszButton']/a[1]").click()
time.sleep(1)
s = driver.find_element_by_id("nr")

Select(s).select_by_visible_text("每页显示50条")
s.click()
time.sleep(1)
driver.find_element_by_class_name("prefpanelgo").click()
time.sleep(1)
a = driver.switch_to_alert()
print(a.text)
# 点确定
a.accept()

# 关闭浏览器
driver.quit()
