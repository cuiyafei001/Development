# coding:utf-8
from bs4 import BeautifulSoup
yo = open("yoyo.html", "r")
# print(yo.read()) # 调试的代码

soup = BeautifulSoup(yo, "html.parser")
# print(soup)  # Soup 整个HTML对象
print(type(soup))
print(soup.head)  # Tag 对象 获取tag里面内容
print(type(soup.head))

print(soup.head.string)  # string对象 获取字符串
print(type(soup.head.string))

print(soup.b.string)   
print(type(soup.b.string))