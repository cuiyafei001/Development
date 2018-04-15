# coding:utf-8

from selenium import webdriver

driver = webdriver.Firefox()

driver.get("https://www.baidu.com")

driver.find_element_by_id("kw").click()

a = driver.find_element_by_id("kw").tag_name
b = driver.find_element_by_id("kw").text