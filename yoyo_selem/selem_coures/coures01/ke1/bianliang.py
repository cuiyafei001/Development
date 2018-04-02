# coding:utf8

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s = 0  # 先给初始值
for i in a:
    print("i 是什么东西呢！！！：%s"%i)
    s = s + i  # 累加
    print(s)

print("最后s的值：%s"%s)



# a = 1  # int
# print(a)
# a = "hello"  # 重新赋值 str
# print(a)
# a = [1, 1]
# print(a)