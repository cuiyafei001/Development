# coding:utf-8


class Sun():

    def __init__(self):
        # 初始化
        self.jinyaoshi = "金钥匙"
        print(self.jinyaoshi)

    def zhaoduixiang(self):
        print(self.jinyaoshi)
        print("开始找对象")


if __name__ == "__main__":
    aa = Sun()   # 实例化的时候，默认执行init里面内容
    aa.zhaoduixiang()
