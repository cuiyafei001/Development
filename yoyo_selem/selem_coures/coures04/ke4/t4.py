# coding:utf-8
from selenium import webdriver

# path = r'C:\Users\Gloria\AppData\Roaming\Mozilla\Firefox\Profiles\1x41j9of.default'
# proffile = webdriver.FirefoxProfile(path)
#
# driver = webdriver.Firefox(proffile)
#
# driver.get("http://www.cnblogs.com/yoyoketang/")


option = webdriver.ChromeOptions()
option.add_argument('--user-data-dir=C:\\Users\\Gloria\\AppData\\Local\\Google\\Chrome\\User Data') #设置成用户自己的数据目录【这里只要到User Data，不是User Data\Default】
driver = webdriver.Chrome(chrome_options=option)
driver.get("http://www.cnblogs.com/yoyoketang/")
