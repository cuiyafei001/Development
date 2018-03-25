#!/usr/bin/env python

# -*- coding: UTF-8 -*-

# 数值运算

print(5 + 4)           # 加法
print(4.3 - 2)         # 减法
print(3 * 7)           # 乘法
print(2 / 4)           # 除法，等到一个浮点数
print(2 // 4)          # 除法，得到一个整数
print(17 % 3 )         # 取余数
print(2 ** 5)          # 乘方

print("========================================")

# 字符串
str = 'Aleen'

print(str)              # 输出字符串
print(str[0:-1])        # 输出第一个到倒数第二个的所有字符
print(str[0])           # 输出字符串第一个字符
print(str[2:5])         # 输出从第三个开始到第五个的字符
print(str[2:])          # 输出从第三个开始的后的所有字符
print(str * 2)          # 输出字符串两次
print(str + "TEST")     # 连接字符串

print("========================================")

# List（列表）
list = ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']

print(list)             # 输出完整列表
print(list[0])          # 输出列表第一个元素
print(list[1:3])        # 从第二个开始输出到第三个元素
print(list[2:])         # 输出从第三个元素开始的所有元素
print(tinylist * 2)     # 输出两次列表
print(list + tinylist)  # 连接列表

a = [1, 2, 3, 4, 5, 6]
a[0] = 9
a[2:5] = [13, 14, 15]
print(a)
a[2:5] = []   # 将对应的元素值设置为 []
print(a)

print("========================================")

# Tuple元组
tup1 = (1,2,3,4)
tup2 = ('asd','zxc')
tup3 = ()               # 空元组
tup4 = (20,)            # 元祖里只有一个元素需要在值后面加上，逗号
print(tup1)             # 输出完整元组
print(tup1[0])          # 输出tup1元组中的第一个指
print(tup1[1:3])        # 输出从第二个元素开始到第三个元素
print(tup1[2:])         # 输出从第三个元素开始的所有元素
print(tup2 * 2)         # 输出两次元组
print(tup1 + tup2)      # 连接元组

for x in (1,2,3):
    print(x)

l = ['ssss','sddd','aaaaa']
print(l[2])
# 奖励表转换为元祖
tuple = tuple(l)
print(tuple)

# 字典d = {key1 : value1,key2 = value2}
dict1 = {'aaa':'123','bbb':'456','ccc':'789'}
# 打印字典里面某个值需要把命名的变量加上打印的值写在['']中
print("dict1['aaa']:",dict1['aaa'])
print("dict1['bbb']:",dict1['bbb'])
print(dict1['aaa'])
# 修改字典
dict1['bbb'] = '666'
print(dict1['bbb'])
# 通过dict创建字典
s = dict(dict1)
print(s)

# 字典的格式化字符串
d = {'a':1,'b':3,'c':9,'d':18} # 字典中的整数值可加可不加引号，字符要加
print(d)
# print('this is %(3)s.' %d)

#  clear函数：清除字典中的所有项
s = {'name1':'aleen','name2':'bob','name3':'cici'}
s3 = {'name4','name5','name6'}
# print(s.clear())
s1 = s.copy()
print(s1)
# fromkeys(指定一个列表，把列表中的值作为字典的key,生成一个字典)
print(dict.fromkeys(s3,26))
# get(指定key，获取对应的值)
print(s.get('name3'))
# items(返回由“键值对组成元素“的列表)
print(s.items())
#  keys(获取字典所有的key)
print(s.keys())
# pop(获取指定key的value，并在字典中删除)
sa = s.pop('name2')
print(sa,s)
# popitem(随机获取某个键值对，并在字典中删除)
sd = s.popitem()
print(s,sd)
# setdefault(获取指定key的value，如果key不存在，则创建)
sf = s.setdefault('name6')
print(sf,s)
# update(添加键 - 值对到字典)
s.update({'name4':'dog'})
print(s)

# 字典内置函数&方法
s6 = {'name1':'www','name2':'eee','name3':'ttt'}
#len()计算字典元素个数，即键的总数。
print(len(s6))
# str(dict)输出字典，以可打印的字符串表示。
print(str(s6))
# 	type(variable)返回输入的变量类型，如果变量是字典就返回字典类型。
print(type(s6))