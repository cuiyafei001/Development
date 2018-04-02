#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import random
# 数据类型
num = 10
num1 = num
# 连续定义多个变量
num2 = num3 = num4 = 1
print(num2)
# id() 函数用于获取对象的内存地址
print(id(num))
print(id(num2))

# 浮点数运算-会存在一定的误差
f1 = 1.1
f2 = 2.2
print(f1+f2)

# 复数：实数部分和虚数部分组成


# 数字类型转换
print(int(1.9))   # int()获取整数部门向下取整
print(float(1))   # float()浮点数转整数
print(str(123))   # 数字转字符串
print(float('123'))  # 字符串转小数
print(int("-123"))    # + - 号作为加减正负的时候才能转换

# 从0-99选取一个随机数
print(random.randrange(100))
# 随机生产[0-1]之间的浮点数
print(random.random())

lis_t = [1, 2, 3, 4, 5]
# 将序列的所有元素随机排序
random.shuffle(lis_t)
print(lis_t)

# 随机生产一个实数 ，他在[3-9]范围
print(random.uniform(3, 9))

print('-------------')
# 运算符表达式
number = 5
number1 = 3
print(number + number1)
print(number - number1)
print(number * number1)
print(number / number1)
print(number % number1)   # 取余数
print(number ** number1)  # 5的三次方
print(number // number1)  # 取整除数

'''
赋值运算符和赋值运算表达式
赋值运算符 = 
赋值运算符表达式
格式：变量 = 表达式
功能：计算了等号右侧‘表达式的值’，并赋值给等号左侧的变量
值： 
'''
a = b = 1 + 2

'''
if 语句
'''
a1 = 10
b1 = 5
c1 = 3
if a1 / b1 > c1:
    print("计算正确")
else:
    print("计算错误")
