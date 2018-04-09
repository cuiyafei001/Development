# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Firefox()


driver.get("https://www.baidu.com/")
time.sleep(3)
ele = driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(ele).perform()
time.sleep(0.5)
driver.find_element_by_link_text("搜索设置").click()

