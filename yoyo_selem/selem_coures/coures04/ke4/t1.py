# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Firefox()


driver.get("https://www.baidu.com/")
time.sleep(3)
ele = driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(ele).perform()
time.sleep(0.5)
driver.find_element_by_link_text("搜索设置").click()
time.sleep(0.5)
s = driver.find_element_by_id("nr")

# Select(s).select_by_index(1)   # 1.索引
# s.click()

# Select(s).select_by_value("50")  # 2.value属性定位
# s.click()

Select(s).select_by_visible_text("每页显示50条")
s.click()

time.sleep(1)

# driver.find_element_by_class_name("prefpanelgo").click()  # 这句没生效

# 当click事件失效的时候，
kuihuabaodian = '$(".prefpanelgo").click()'  # 95%以上会生效
driver.execute_script(kuihuabaodian)

time.sleep(0.5)
a = driver.switch_to_alert()
print(a.text)  # 获取文本
a.accept()  # 点确定




