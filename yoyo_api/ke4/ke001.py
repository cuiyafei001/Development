#!/usr/bin/env python

# -*- coding: UTF-8 -*-

import requests
import urllib3
# 出现InsecureRequestWarning(警告)就导入urllib3加上这句话
urllib3.disable_warnings()

# 博客园添加cookie绕过验证码登录
url = "https://i.cnblogs.com/EditPosts.aspx?opt=1"

# https协议在参数里加verify=False不去验证SSL证书
r = requests.get(url,verify=False)
# print(r.text)

# .Cnblogs.AspNetCore.Cookies=CfDJ8Gf3jjv4cttDnEy2UYRcGZ37JHwn4dDoJvdDoK-O8Lwl-cePzv0YocoMxTivBGOre0SsOjF9ieKuPRapKTqQmfrEIs0UZGImCr-x4HpBJyVaolD_-dvXItjYZVzJCrUTYtkZwtk8eQcEd7u1nyI0mYjjio9T-StVrZAGSTKC2x5RTvR9nXozY8LnfxfOq8YmeVgbBNFkQ6cjZXzflwGOEfgH-HyMqhE14gohW5SGp4eNqJPikVuYDb2PAlHaZFFVjxV1T-SpSas2bktjXR-LSGDfn_-yDlIvPQ_wtVwvEMlohs8kjf4IuTdARN2mkFG8vw
# 编辑器识别不到cookies，不用管他
c = requests.cookies.RequestsCookieJar() # jar包装东西篮子
print(c)

# cookie 有时候有很多个需要试几次看哪个是记住登录的cookie
# c.set(".Cnblogs.AspNetCore.Cookies","CfDJ8Gf3jjv4cttDnEy2UYRcGZ37JHwn4dDoJvdDoK-O8Lwl"
#                                     "-cePzv0YocoMxTivBGOre0SsOjF9ieKuPRapKTqQmfrEIs0UZGImCr"
#                                     "-x4HpBJyVaolD_-dvXItjYZVzJCrUTYtkZwtk8eQcEd7u1nyI0mYjjio9T"
#                                     "-StVrZAGSTKC2x5RTvR9nXozY8LnfxfOq8YmeVgbBNFkQ6cjZXzflwGOEfgH"
#                                     "-HyMqhE14gohW5SGp4eNqJPikVuYDb2PAlHaZFFVjxV1T-SpSas2bktjXR-"
#                                     "LSGDfn_-yDlIvPQ_wtVwvEMlohs8kjf4IuTdARN2mkFG8vw")
c.set(".CNBlogsCookie","56EDEB670276E30AF95C34CC6A01E5497669BF838FD4F116F22B973A6A3EA88"
                         "A088836EFAAAFE3B396C434BB9CEDA04FDD0A4B520BAFE45911C7C408042D08B36"
                         "302041A46E18724D8D9BC53B4443F6B97C6708D")
print(c) # 在jar篮子里装了一个东西

# r.cookies.update(c) # 更新cookies的信息
# print(r.cookies)

# 访问登录之后的请求
url1 = "https://i.cnblogs.com/EditPosts.aspx?opt=1"

# 如果有头部信息就单独传头部，cookies单独剥离出来单独传
h = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
    }
r1 = requests.get(url1,verify=False,cookies=c,headers=h)
print(r1.text)