from yoyo_selem_coures.selem_coures.coures07.ke7.t3 import Father, Mother


class Sunnew(Father,Mother):
    def fangzi(self):
        print("儿子把父亲的房子拆了，重新建房子") # print是没实际功能，心理作用

    def quxifu(self):
        self.piaozi()
        self.chezi()
        self.fangzi()


if __name__ == "__main__":
    s = Sunnew()
    s.quxifu()
