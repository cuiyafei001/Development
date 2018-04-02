# coding:utf-8
import requests
from bs4 import BeautifulSoup
r = requests.get("https://www.qiushibaike.com/")
m = r.content.decode("utf-8")

soup = BeautifulSoup(m, "html.parser")

texts = soup.find_all() # 返回的是list
for i in texts:
    print(i.span.get_text().replace("\n", ""))