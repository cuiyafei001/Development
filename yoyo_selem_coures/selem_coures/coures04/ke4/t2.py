# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Firefox()


driver.get("https://www.baidu.com/")
time.sleep(3)

t = driver.find_elements_by_class_name('mnav')[0]
print(t.text)  # 实际结果
if t.text == "新闻":
    print("测试通过：pass!")
else:
    print("测试失败：fail!")

url = t.get_attribute("href")
print(url)
if url == "http://news.baidu.com/":
    print("测试通过：pass!")
else:
    print("测试失败：fail!")

name = t.get_attribute("name")
print(name)

tag = t.tag_name  # 获取标签属性




