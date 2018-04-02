# coding:utf-8
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://www.baidu.com")

# element = driver.find_element_by_id("kw")  # 单数定位
# print(element)
#
# elements = driver.find_elements_by_id("kw")  #复数定位
# print(elements)
# print(type(elements))   # 数据类型
# elements[0].send_keys("中文")

elements = driver.find_elements_by_class_name("mnav")
print(len(elements))  # 定位到了几个
a = 2
if len(elements) > 2:
    elements[a].click()

