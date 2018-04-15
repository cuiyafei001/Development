# coding:utf-8

# object 是所以类的一个基类


class Bird(object):

    def zuiba(self):
        print("可以吃虫子")

    def chibang(self):
        print("翅膀可以飞")

    def jiao(self):
        print("爪子可以抓东西")


if __name__ == "__main__":
    b = Bird()   # 创建一个实例
    b.zuiba()
    b.jiao()
    c = Bird()  # 创建另外一个实例
    c.zuiba()
    b.zuiba()


