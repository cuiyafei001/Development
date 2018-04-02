# coding:utf-8

a = None   # None
b = True  # bool
c = 12    # int
d = 12.3  # float
e = "123avds"  # str
f = [1,2,3,12.3,None,"213",[1,2]] # list
g =(1,3,"a","bc")  # tuple
# 字典的特征：{ }，无序的，key:value, key是唯一的
h = {
    "a": 12,
    "b": "11",
    }

# type函数查看数据类型
print(type(g))

# 字典的增删改查
h["c"] = 12345
print(h)

del(h["a"])  # 加不加括号都可以
print(h)

h["b"] = "abc"
print(h)

print(h["b"])










