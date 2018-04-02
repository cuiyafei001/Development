# coding:utf-8

# 实现a的平方减去b的平方 （a+b)*(a-b)

def jia(a=1, b=0):  # 传形参
    return a+b

def jian(a,b):
    return a-b

def chengfa(a,b):
    return a*b

if __name__ =="__main__":
    sum = jia(5, 4)
    cha = jian(5, 4)
    pz = chengfa(sum, cha)
    print(pz)