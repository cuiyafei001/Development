# coding:utf-8
from selenium import webdriver
import time
# 打开浏览器
driver = webdriver.Firefox()  # 打开浏览器
# driver = webdriver.Chrome()

# sleep休眠
time.sleep(3)
driver.get("https://www.baidu.com")
time.sleep(3)
driver.get("http://www.cnblogs.com/yoyoketang")
time.sleep(3)
driver.back()  # 返回上一页
time.sleep(3)
# 下一页
driver.forward() # 下一页
# 刷新
driver.refresh()
time.sleep(3)
driver.quit()   # 退出浏览器，清空缓存

