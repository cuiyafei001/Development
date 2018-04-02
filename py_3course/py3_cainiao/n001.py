#!/usr/bin/env python

# -*- coding: UTF-8 -*-

# 单行注释以 # 开头
# 第一个注释
print ("Hello, Python!") # 第二个注释

'''
第三注释
第四注释
'''

"""
第五注释
第六注释
"""
print ("Hello, Python!")

# 缩进要保持一致不然会报错
if True:
    print ("True")
else:
    print ("False")

if True:
    print ("Answer")
    print ("True")
else:
    print ("Answer")
    print ("False")

# 多行语句
# Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠(\)来实现多行语句，例如：

# total = item_one + \
#         item_two + \
#         item_three
# 在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)，例如：

total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']

# 数字(Number)类型
# python中数字有四种类型：整数、长整数、浮点数和复数。
# int (整数), 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
# bool (布尔),如 true。
# float (浮点数), 如 1.23、3E-2
# complex (复数), 如 1 + 2j、 1.1 + 2.2j

# 字符串
word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
可以由多行组成"""

str='Runoob'

print(str)                 # 输出字符串
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第五个的字符
print(str[2:])             # 输出从第三个开始的后的所有字符
print(str * 2)              # 输出字符串两次
print(str + '你好')        # 连接字符串

print('------------------------------')

print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

# 等待用户输入
input("\n\n按下 enter 键后退出。")

# 同一行显示多条语句
import sys; x = 'runoob'; sys.stdout.write(x + '\n')

# import 与 from...import
# 在 python 用 import 或者 from...import 来导入相应的模块。
# 将整个模块(somemodule)导入，格式为： import somemodule
# 从某个模块中导入某个函数,格式为： from somemodule import somefunction
# 从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
# 将某个模块中的全部函数导入，格式为： from somemodule import *
# 导入sys模块
import sys
print('================Python import mode==========================')
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)