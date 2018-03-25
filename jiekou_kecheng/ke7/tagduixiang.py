# coding:utf-8

from bs4 import BeautifulSoup
yo = open("yoyo.html", "r")

soup = BeautifulSoup(yo, "html.parser")
p = soup.p  # 找到p标签
print(p)

print(p.name)  # 获取tag名称
print(p.string)  # str
print(p["class"])  # class返回的是list
print(type(p["class"]))
print(p["id"])  # id
print(p.attrs)  # 返回的字典，获取所有的属性
print(type(p.attrs))

