# coding:utf-8
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://mail.126.com/")
time.sleep(3)

# 切换iframe
# 1.有id，并且唯一，直接写id
# driver.switch_to_frame("x-URS-iframe")
# # 2.有name，并且唯一，直接写name
# driver.switch_to_frame("xxxx")
# 3.无id,无name,先定位iframe元素
# iframe = driver.find_elements_by_tag_name("iframe")[0]
# driver.switch_to_frame(iframe)
# 4.通过index索引定位
# driver.switch_to_frame(2)  # 从0开始
#
# driver.find_element_by_name("email").send_keys("123456")
#
# # 退出iframe，再操作
# driver.switch_to_default_content()  # 回到主页面

# driver.switch_to_frame("f1")
# # 操作元素
# driver.switch_to_default_content()
# driver.switch_to_frame("f2")

# 嵌套
driver.switch_to_frame("f1")
driver.switch_to_frame("f2")
# driver.switch_to.parent_frame()  # 回到f1
driver.switch_to_default_content()  # 回到主页面





