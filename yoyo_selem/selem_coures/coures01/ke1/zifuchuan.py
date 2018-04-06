# bool

a = 0
print(bool(a))
b = -12
print(bool(b))

s1 = "hello 1222 world!"

print(len(s1))

print(s1.count("l"))  # 统计某个字符出现次数
# 切片内容索引都是从0开始0代表第一个
print(s1[0:5])   # 前闭后开区间 [0:4)
print(s1[:5])    # 从第一个开始切到第五个
print(s1[2:5])   # 从第二个开始切到
print(s1[6:])    # 从第六个开始到最后一个
print(s1[::-1])  # 反转字符串
print(s1[6:3:-1])  # 反转字符串

# a = "hello"
# b = "world"
# print(a*3)

ls = [1, 45, 'asc', '我', 8]
print(ls[::-1])
print(ls[1:3])
print(ls[3:])

tup = (12, '你是谁', 55, 454, '号码')
print(tup[3:])
