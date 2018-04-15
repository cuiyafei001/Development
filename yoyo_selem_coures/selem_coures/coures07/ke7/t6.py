# coding:utf-8
from yoyo_selem_coures.selem_coures.coures07.ke7.t3 import Father, Mother


class People(Father,Mother):
    def __init__(self, xingbie, live):  # 参数
        self.sex = xingbie
        self.live = live
        self.age = 18
        self.duixiang = self.zhaoduixiang()

    def age_n(self):
        return self.age

    def zhaoduixiang(self):
        print("找对象的要求1：%s" % self.sex)
        print("找对象的要求2：%s" % self.live)
        print("找对象的要求2：%s" % self.age)
        # 实例方法可以调用静态方法
        self.jintai()
        self.__sifangqian()   # 自己的私房钱

    @staticmethod
    def jintai():  # 类里面的函数叫静态方法
        # 静态方法 跟函数功能是一样的
        # 没有参数
        print("hello world!")

        # 静态方法是不能调用实例方法的

    def __sifangqian(self):
        # 私有方法
        print("我的私房钱")


if __name__ == "__main__":
    People.jintai()  # 1.不需要实例化可以调用

    a = People("girl", "live")
    print(a.sex)  # 属性
    print(a.age)
    print(a.duixiang)
    print(a.age_n())
    print(a.jintai())  # 2.实例化也是可以调用的

