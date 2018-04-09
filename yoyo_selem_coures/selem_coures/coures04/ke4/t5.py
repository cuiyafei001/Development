# coding:utf-8
from selenium import webdriver
import time
path = r'C:\Users\Gloria\AppData\Roaming\Mozilla\Firefox\Profiles\1x41j9of.default'
proffile = webdriver.FirefoxProfile(path)

driver = webdriver.Firefox(proffile)

# 加载配置文件后，已经登录成功
driver.get("http://www.cnblogs.com/yoyoketang/")

time.sleep(3)
# 点新随笔
driver.find_element_by_id("blog_nav_newpost").click()
time.sleep(2)
driver.find_element_by_xpath(".//*[@id='Editor_Edit_EditorBody_uploadImage']/span[1]/img").click()
time.sleep(4)
# 定位所有iframe,取第二个
iframe = driver.find_elements_by_tag_name('iframe')[1]
# 切换到iframe上
driver.switch_to_frame(iframe)

driver.find_element_by_css_selector('input[name="file"]').send_keys("D:\\1.png")
driver.switch_to_default_content()
