from yoyo_selem_coures.selem_coures.coures07.ke7.t3 import Father, Mother


class People(Father,Mother):
    def __init__(self, xingbie, live):  # 参数
        self.sex = xingbie
        self.live = live

    def zhaoduixiang(self,age):
        print("找对象的要求1：%s" % self.sex)
        print("找对象的要求2：%s" % self.live)
        print("找对象的要求2：%s" % age)


class Sun(People):
    pass


if __name__ == "__main__":
    # a = People("girl", "活的")  # 实例化的时候调用参数
    # a.zhaoduixiang(18)
    b = Sun("girl", "活的")
    b.zhaoduixiang(18)
    b.fangzi()
    b.chezi()
