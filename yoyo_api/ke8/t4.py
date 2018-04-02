# coding:utf-8

class Qie(object):

    def __init__(self, n):  # 初始化
        print("当它实例化的时候，先运行初始化东西")
        self.name = n
        self.__age = "18"  # 私有属性

    def zuiba(self):  # 类本身的实例参数
        print("吃饭")

    def tui(self):
        print("约会")

    def chifan(self):
        self.zuiba()

    def xiaokeai(self):
        a = self.name
        b = self.__age

if __name__ == "__main__":
    QQ1 = Qie("小可爱")  # 实例化



