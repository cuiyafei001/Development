#!/usr/bin/env python
# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("http://www.51lianying.com/")
time.sleep(3)

driver.find_element_by_link_text("登录").click()
driver.find_element_by_name("username").clear()
driver.find_element_by_name("password").clear()
time.sleep(1)
driver.find_element_by_name("username").send_keys("13123943996")
driver.find_element_by_name("password").send_keys("123456")
time.sleep(1)
driver.find_element_by_css_selector("#btn-login").send_keys(Keys.ENTER)
driver.find_element_by_css_selector("#btn-login").click()
