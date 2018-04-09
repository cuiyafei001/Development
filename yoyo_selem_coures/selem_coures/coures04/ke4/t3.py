# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Firefox()


driver.get("https://www.baidu.com/")
time.sleep(3)
# ele = driver.find_element_by_link_text("设置")
# ActionChains(driver).move_to_element(ele).perform()
# time.sleep(0.5)
# s = driver.find_element_by_link_text("搜索设置")
# print(s.is_displayed())   #  判断隐藏和显示

si = driver.find_element_by_id("su").size
print(si['height'])
print(si['width'])

print(driver.name)    # 浏览器名称

print(driver.title)  # 获取title

print(driver.current_url)  # 获取当前浏览器的url

print(driver.page_source)  # 获取整个html



