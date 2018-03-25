# coding:utf-8
import unittest
from common import HTMLTestRunner

# 存放用例的路径
# casepath = r"D:\newtestapi\case"

import os
print(__file__)
basepath = os.path.realpath(os.path.dirname(__file__))
print(basepath)
casepath = os.path.join(basepath, "case")
reportpath = os.path.join(basepath, "report")
print(reportpath)

# 三要素：第一看有没用例，第二看用例的路径，第三看匹配规则
discover = unittest.defaultTestLoader.discover(casepath, "test*.py")
print(discover)  # 看有没找到用例

# import time
# nowtime = time.strftime("%Y_%m_%d_%H_%M_%S")
# print(nowtime)

# 确定生成html报告的地址
htmlpath = os.path.join(reportpath, "result.html")

print(htmlpath)

rp = open(htmlpath, "wb")  # 打开文件写入

# 运行器
runner = HTMLTestRunner.HTMLTestRunner(rp,
                                       title="报告的标题",
                                       description="报告的描述"
                                       )
runner.run(discover)







