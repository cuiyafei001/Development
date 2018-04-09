# coding:utf-8
from selenium import webdriver
import time
driver = webdriver.Firefox()
# driver.get("https://tieba.baidu.com/index.html")
# time.sleep(3)
# driver.find_element_by_name("kw1").send_keys("好的")

driver.get("https://www.baidu.com/")
# driver.find_element_by_class_name("s_ipt").send_keys("haha")

# t = driver.find_element_by_tag_name("body").text   # text获取元素文本
# print(t)

# driver.find_element_by_link_text("新闻").click()

# driver.find_element_by_xpath(".//*[@id='u1']/a[3]").click()

driver.find_element_by_css_selector(".s_ipt").send_keys("好的")