# coding:utf-8

import requests
import urllib3
urllib3.disable_warnings()

s = requests.session()  # 当成一个无界面的，微型浏览器
print("没有发请求之前的cookie")
print(s.cookies)

url = "https://i.cnblogs.com/EditPosts.aspx?opt=1"
r1 = s.get(url, verify=False)

print("发了一个请求之后由于没登录cookie没变化")
print(s.cookies)

# 登录的cookies
c = requests.cookies.RequestsCookieJar()  # 装东西的盒子
c.set(".Cnblogs.AspNetCore.Cookies", "CfDJ8Gf3jjv4cttDnEy2UYRcGZ2JJtCOSvXC9kUtfPfXK2_3m4bQwpTtKHVUMHrO145IQ_9_QOzfpAe61gQgxNmzK1q43P_McONPOq"
                                         "jy5HnjOH8WYkM-A20WFlN3JtiElYtluuSuPZZGA9DGgi2eBNUbNI0uLgCSnvJK1Vj91W9WefUkLbtT8QE2LH2ptZ_Hti7ccu0yCBGcppKQLUTpWltssuj"
                                         "-yuWJBw6CRS6nnMbbRQZ-bBte2QlJTUTtQkLHjrpW725H5qBK-eGba-YnMQT3fXDdlZSm9PGnQ383lND1MtASkeXE9O4JO8O02kdZFFYuAQ")
c.set(".CNBlogsCookie", "E3954454761B8601ABC025BCCF0DD91AF850D84D7CFF1D0A7D78D95DE2EBF22DBCC616599F070C63D31C43A6987615FAB4FF041E021C6001DC"
                            "D951D7C31025D43A3480BD338A8C4776C8F673018F334395A7A2C9")

s.cookies.update(c)  # 更新添加登录的cookies

print("添加之后再看下浏览器的cookies")
print(s.cookies)

# 接下来再用浏览器发请求
r2 = s.get(url, verify=False)
# print(r2.text)

r3 = s.get("https://i.cnblogs.com/Configure.aspx", verify=False)
print(r3.text)
