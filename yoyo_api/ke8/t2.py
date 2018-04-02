# coding:utf-8
#
# a = [1, 2, 3, 5, 6, 9, 7]
# print(len(a))  # len就是一个函数
#
# # s = 0
# # for i in a:
# #     s+=i
# # print(s)
#
# print(sum(a))
#
# a.sort()
# print(a)

def login(username,psw):
    if username != "admin":
        print("账号错了") # print没任何功能，只是显示在控制台
    elif psw != "111111":
        print("密码错了")
    elif username == "admin" and psw == "111111":
        return "token:zxzxzxzxzxzxzxzxzxzx"
    else:
        print("账号不存在")
if __name__ == "__main__":
    res = login("admin", "111111")  # 返回的是字符串
    print(res)
