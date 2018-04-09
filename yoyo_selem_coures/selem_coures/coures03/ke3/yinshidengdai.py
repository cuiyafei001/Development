# coding:utf-8
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
# 隐式等待30s
driver.implicitly_wait(30)  # 全局生效，不是万能的
print(driver.title)
driver.find_element_by_id("kw").send_keys("hahha")
time.sleep(1)
print(driver.title)

# 如果页面一直转圈圈，js出错了。







