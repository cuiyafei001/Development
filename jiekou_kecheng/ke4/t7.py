# coding=utf-8
from selenium import webdriver

def sele_login():
    # 配置文件地址，你自己浏览器地址：设置-故障排除-配置文件夹
    profile_directory = r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\nwi4vflo.default'
    # 加载配置配置
    profile = webdriver.FirefoxProfile(profile_directory)
    # 启动浏览器配置
    driver = webdriver.Firefox(profile)

    url = "http://www.cnblogs.com/yoyoketang/"
    driver.get(url)

    cooks = driver.get_cookies()
    print(cooks)  # list对象
    driver.quit()  # 退出浏览器
    return cooks


import requests
import urllib3
urllib3.disable_warnings()

url = "https://passport.cnblogs.com/user/signin"
headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"
           }  # get方法加个ser-Agent就可以了

s = requests.session()

cooks = sele_login()

# 添加登录需要的两个cookie
c = requests.cookies.RequestsCookieJar()
for i in cooks:
    c.set(i['name'], i['value'])
print(c)
s.cookies.update(c)  # 更新cookies

# 验证是否登录成功

r1 = s.get("https://i.cnblogs.com/EditPosts.aspx?opt=1", headers=headers, verify=False)
print(r1.text)

