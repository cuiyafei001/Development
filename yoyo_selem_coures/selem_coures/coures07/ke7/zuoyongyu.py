# coding:utf-8

a = 1  # 整个脚本全局的


def add():
    b = 4   # 函数下生效，局部变量
    a = 2  # 局部的变量
    c = a+3+b
    return c


for i in range(10):  # [0,9)
    a = a+i

print(a)

if __name__ == "__main__":
    print(add())
