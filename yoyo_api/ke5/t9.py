# coding:utf-8

import requests
import urllib3
urllib3.disable_warnings()

s = requests.session()  # 当成一个无界面的，微型浏览器
print("没有发请求之前：-0-----")
print(s.cookies)

url = "https://i.cnblogs.com/EditPosts.aspx?opt=1"
r1 = s.get(url, verify=False)

print("随便发了一个请求之后，cookies变化----------")
print(s.cookies)

# 登录的cookies
c = requests.cookies.RequestsCookieJar()  # 装鸡蛋的篮子
c.set(".Cnblogs.AspNetCore.Cookies", "xxxx")
c.set(".CNBlogsCookie", "xxxxxxxxx")

s.cookies.update(c)  # 更新添加登录的cookies

print("添加之后再看下浏览器的cookies")
print(s.cookies)

# 发帖
url1 = "https://i.cnblogs.com/EditPosts.aspx"
par = {"opt": "1"}
body = {
    "__VIEWSTATE": "",
    "__VIEWSTATEGENERATOR0":"FE27D343",
    "Editor$Edit$txbTitle":"fffggggf",
    "Editor$Edit$EditorBody":"22222222222",
    "Editor$Edit$Advanced$ckbPublished":"on",
    "Editor$Edit$Advanced$chkDisplayHomePage":"on",
    "Editor$Edit$Advanced$chkComments":"on",
    "Editor$Edit$Advanced$chkMainSyndication":"on",
    "Editor$Edit$Advanced$txbEntryName":"",
    "Editor$Edit$Advanced$txbExcerpt":"",
    "Editor$Edit$Advanced$txbTag":"",
    "Editor$Edit$Advanced$tbEnryPassword":"",
    "Editor$Edit$lkbDraft":"存为草稿"
}

r1 = s.post(url1,params=par, data=body, verify=False)
print(r1.url)

# 正则提取
import re
# 知道前后取中间 如：postid=8546254&

postid = re.findall("postid=(.+?)&", r1.url)[0]
print(postid)

# 删除的接口
url2 = "https://i.cnblogs.com/post/delete"
body1 = {
    "postId": postid
}
r2 = s.post(url2, json=body1)
result = r2.json()["isSuccess"]
print(result)  # True才是成功了

assert result==True









