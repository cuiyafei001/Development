# coding:utf-8
import requests
from bs4 import BeautifulSoup
r = requests.get("http://699pic.com/sousuo-218808-13-1-0-0-0.html")
m = r.content.decode("utf-8")

soup = BeautifulSoup(m, "html.parser")
all = soup.find_all(class_="lazy")

for i in all:
    # print(i["data-original"])
    try:
        url = i["data-original"]
        print(url)
        name = i["title"]
        print(name)
        r1 = requests.get(url)
        path = "D:\\test11"
        import os
        if not os.path.exists(path):
            os.mkdir(path)
        fp = open(path+"\\%s.jpg"%name, "wb")

        fp.write(r1.content)  # r1.content获取的是二进制流
        fp.close()
    except Exception as msg:
        print(msg)







