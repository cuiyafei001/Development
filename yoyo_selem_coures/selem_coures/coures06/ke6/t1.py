a = [1, 3, 4, 5, 6, 9, 10]

print(len(a))  # len函数

print(sum(a))  # sum函数


def he(aaaa):
    '''求和的函数'''
    s = 0    # 局部变量
    for i in aaaa:
        s=s+i
    return s   # 如果没有return 返回None


print(he(a))

b = "中文"  #
print(type(b)) # unicode
print(ascii(b))

d = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
c = list(range(10))  # list
print(c)
# 转化成元组
print(tuple(c))

import random

e = random.randint(1,10)
print(e)


h = [0, 1, 2, 3, 4, 5, 6, 7, 8]
k = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

for i, j in zip(h, k):
    print(j+str(i))





