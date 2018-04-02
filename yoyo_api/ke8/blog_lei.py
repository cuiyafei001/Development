# coding:utf-8
import re
import requests
import urllib3
urllib3.disable_warnings()
import time

nowtime = time.strftime("%Y_%m_%d_%H_%M_%S")

# s = requests.session()  # 当成一个无界面的，微型浏览器
class Blog():
    def __init__(self, s):
        self.s = s

    def login(self):
        # 登录的cookies
        c = requests.cookies.RequestsCookieJar()  # 装鸡蛋的篮子
        c.set(".Cnblogs.AspNetCore.Cookies", "自己抓包")
        c.set(".CNBlogsCookie", "自己抓包")
        self.s.cookies.update(c)  # 更新添加登录的cookies

        url = "https://i.cnblogs.com/EditPosts.aspx?opt=1"
        r1 = self.s.get(url, verify=False)
        # print(r1.text)
        if "博客后台管理 - 博客园" in r1.text:
            print("登录成功了！！！")
        else:
            print("登录失败了")
        return r1.text

    def fatie(self):
        # 发帖
        url1 = "https://i.cnblogs.com/EditPosts.aspx"
        par = {"opt": "1"}
        body = {
            "__VIEWSTATE": "",
            "__VIEWSTATEGENERATOR0":"FE27D343",
            "Editor$Edit$txbTitle":"fffgggg%s"%nowtime,
            "Editor$Edit$EditorBody":"22222222%s"%nowtime,
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

        r2 = self.s.post(url1, params=par, data=body, verify=False)
        print(r2.url)
        return r2.url

    def get_postid(self, re_url):
        # 正则提取
        # 知道前后取中间 如：postid=8546254&
        postid = re.findall("postid=(.+?)&", re_url)[0]
        print(postid)
        return postid

    def delet_tie(self, postid):
        # 删除的接口
        url2 = "https://i.cnblogs.com/post/delete"
        body1 = {
            "postId": postid
        }
        r2 = self.s.post(url2, json=body1)
        result = r2.json()["isSuccess"]
        # print(result)  # True才是成功了
        return result

if __name__ == "__main__":
    s = requests.session()
    blog = Blog(s)
    blog.login()
    re_url = blog.fatie()
    postid = blog.get_postid(re_url)
    r = blog.delet_tie(postid)
    print(r)




