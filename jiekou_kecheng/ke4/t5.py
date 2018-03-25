# coding:utf-8
import requests
import urllib3
urllib3.disable_warnings()

host = "https://i.cnblogs.com/"

s = requests.session()


url = host+"EditPosts.aspx?opt=1"

r1 = s.get(url, verify=False)
print(r1.url)  # 查看返回的URL
print(r1.status_code)

# # 禁止重定向，找到中间的地址
# r2 = s.get(url, verify=False, allow_redirects=False)
# print(r2.status_code)
# print(r2.url)
# print(r2.headers['Location'])
#
# # 重定向后的地址
# print(host+r2.headers['Location'])  # urlencode编码


# history
print(r1.history)

for i in r1.history:
    print(i.status_code)
    print(i.url)
    print(i.headers)
    print(i.text)


