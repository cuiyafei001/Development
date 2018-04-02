# coding:utf-8
import requests
import urllib3
urllib3.disable_warnings()

url = "https://i.cnblogs.com/EditPosts.aspx?opt=1"
r = requests.get(url, verify=False)
print(r.cookies)
# print(r.text)

# 编辑器没识别到，不用管
c = requests.cookies.RequestsCookieJar()  # 装鸡蛋的篮子
print(c)
# c.set(".Cnblogs.AspNetCore.Cookies", "CfDJ8Gf3jjv4cttDnEy2UYRcGZ2JJtCOSvXC9kUtfPfXK2_3m4bQwpTtKHVUMHrO145IQ_9_QOzfpAe61gQgxNmzK1q43P_McONPOq"
#                                          "jy5HnjOH8WYkM-A20WFlN3JtiElYtluuSuPZZGA9DGgi2eBNUbNI0uLgCSnvJK1Vj91W9WefUkLbtT8QE2LH2ptZ_Hti7ccu0yCBGcppKQLUTpWltssuj"
#                                          "-yuWJBw6CRS6nnMbbRQZ-bBte2QlJTUTtQkLHjrpW725H5qBK-eGba-YnMQT3fXDdlZSm9PGnQ383lND1MtASkeXE9O4JO8O02kdZFFYuAQ")
c.set(".CNBlogsCookie", "E3954454761B8601ABC025BCCF0DD91AF850D84D7CFF1D0A7D78D95DE2EBF22DBCC616599F070C63D31C43A6987615FAB4FF041E021C6001DC"
                            "D951D7C31025D43A3480BD338A8C4776C8F673018F334395A7A2C9")

# 如果想加cookie的其它属性
# c.set(".CNBlogsCookie", "xxxxxxxxx", expiry=1554959887, httpOnly=True)

print(c)  # 加了一个鸡蛋了 Jar

# 把一篮子鸡蛋煮熟变成卤鸡蛋
d = dict(c)  # 字典
print("鸡蛋煮熟了:-----------")
print(d)


# 访问登录之后的请求
url1 = "https://i.cnblogs.com/EditPosts.aspx?opt=1"

h = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
}

r1 = requests.get(url1, verify=False, cookies=c, headers=h)
# print(r1.text)
#
#





