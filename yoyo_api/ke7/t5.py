# coding:utf-8
import requests
from bs4 import BeautifulSoup
r = requests.get("http://www.cnblogs.com/yoyoketang/p/")
m = r.content.decode("utf-8")

soup = BeautifulSoup(m, "html.parser")
# a = soup.find(class_="PostList")
# print(a.div.a.string)

all = soup.find_all(class_="PostList")  # list

print(all[2])
# for i in all:
#     print(i.div.a.string)