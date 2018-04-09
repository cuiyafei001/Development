# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import time
driver = webdriver.Firefox()

driver.get("https://www.baidu.com/")
time.sleep(5)
driver.find_element_by_id("kw").send_keys("中文内容")
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
