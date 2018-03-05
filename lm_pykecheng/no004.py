# coding=utf-8

l = [1, 5, 3, 7, "ffff", 4.3, "hello"]
print(l)
l.append("good") # 在列表后面添加一个元素
print(l)
del l[2] # 删除一个元素,删除元素到位置
print(l)
l.remove("ffff") # 移除一个元素，移除元素，存在列表中的元素
print(l)
l[2]="input" # 给制定的元素，重新赋值
print(l)
o = l.pop(3)
print(l)
print(o)
print(len(l))
li = [6, 2, 6,11,44 ,55,0,7]
li.sort()
print(li)
print(li.count(6))
