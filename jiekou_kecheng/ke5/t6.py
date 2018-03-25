# coding:utf-8
import requests
url = "http://www.kuaidi.com/index-ajaxselectcourierinfo-1202247993797-yunda.html"
r = requests.get(url)
print(r.json()["data"][1]["context"])

