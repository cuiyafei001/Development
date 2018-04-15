# coding:utf-8


class Father():

    def fangzi(self):
        print("父亲的房子")

    def chezi(self):
        print("父亲的车子")


class Mother():

    def piaozi(self):
        print("妈妈的票子")


class sun(Father,Mother):

    def quxifu(self):
        fang = self.fangzi()
        che = self.chezi()
        piao = self.piaozi()


if __name__ == "__main__":
    s = sun()
    s.quxifu()
