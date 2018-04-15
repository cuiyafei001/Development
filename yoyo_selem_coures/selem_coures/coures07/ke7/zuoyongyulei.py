# coding:utf-8

a = 1  # 整个脚本全局

class People():
    b = 2  # 整个类的变量，类里面全局

    def __init__(self):
        c = 3   # 局部的，只在init生效
        self.d = 4  # 加了self就是类里面全局的
        self.e = 5

    # def add(self):
    #     self.e = 5
    #     print("a的值：%s"%a)
    #     print("b的值：%s"%self.b)
    #     # print("b的值：%s"%c)  # 调用不到
    #     print("d的值：%s"%self.d)
    #     print("d的值：%s"%self.e)

    def acc(self):
        print(self.e)

    def aff(self):
        print(self.e)


if __name__ == "__main__":
    aaa = People()
    aaa.add()
