#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
time.sleep(3)

driver.find_element_by_id("kw").send_keys("百度")
driver.find_element_by_id("su").click()
time.sleep(1)

handle = driver.current_window_handle    # 获取当前窗口handle
print("获取当前handle: %s" % handle)
print(driver.title)
driver.find_element_by_xpath(".//*[@id='3']/h3/a").click()
time.sleep(3)

handle1 = driver.current_window_handle   # 点击之后的handle
print("选择一个元素点击后的窗口 handle: %s" % handle1)
print(driver.title)

# 获取所有handle
all_h = driver.window_handles
print(all_h)

# 根据索引切换到最新打开的窗口
driver.switch_to.window(all_h[-1])
# print("当前页面handle：%s" % all_h[-1])
print(driver.title)

# 切换到首页
driver.switch_to.window(handle)
print(driver.title)
driver.quit()
