# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
driver = webdriver.Firefox()
driver.get("https://tieba.baidu.com/index.html")

# time.sleep(2)
# # class 属性有空格的时候
# driver.find_element_by_class_name("search_ipt").send_keys("取其中一个class")

# driver.find_element(By.CLASS_NAME, "search_ipt").send_keys("By定位的")
driver.find_element_by_class_name("search_ipt").send_keys("取其中一个class")

driver.find_element_by_class_name("search_ipt").submit()   # 模拟回车键


