# coding:utf-8
a = 1  # 有等号就是实参
# 求a的平方-b的平方  (a+b)*(a-b)


class Bird():  # 抽象的
    # slef是类本身的实例参数
    def add(self, a=0, b=0):  # 方法
        return a+b

    def jian(self, a,b):
        return a-b

    def cheng(self, a,b):
        return a*b

    def chengfa(self):
        self.cheng(self.add(3, 2),  self.jian(3, 2))


if __name__ == "__main__":
    shili = Bird()  # 实例化过程
    print(type(shili))
    shili.add()

    # Bird.add()  # 这个是不合法的
    # Bird().jian()



#
# # a =10 , b =5
#
# c = add(a = 5 , b =10)
# d = jian(a =5 , b =10)
# result = cheng(c,d)
# print(result)
# print(10**4)
