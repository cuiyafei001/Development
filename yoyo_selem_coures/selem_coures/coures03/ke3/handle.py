# coding:utf-8
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://bj.ganji.com/")
time.sleep(3)
handle = driver.current_window_handle  # 获取当前的handle
print("获取到当前的handle:%s"%handle)
print(driver.title)
driver.find_elements_by_class_name("dt-t")[0].click()

handle1 = driver.current_window_handle  # 获取当前的handle
print("点完之后当前的handle:%s"%handle1)

handles = driver.window_handles  # 获取全部的
print(handles)
print(type(handles))


# driver.switch_to_window(handles[-1])   # 切换过去了
driver.switch_to.window(handles[-1])


time.sleep(3)
print(driver.title)

# 新页面元素操作完了，关掉了，回到主页面
driver.close()  # 关闭当前窗口
driver.switch_to_window(handle)
time.sleep(3)
print(driver.title)

driver.find_elements_by_class_name("dt-t")[1].click()

# 复数定位的时候，如果页面无刷新，可以直接用一次定位复数的list

# 页面有刷新的时候，需重新再次定位

driver.quit()
