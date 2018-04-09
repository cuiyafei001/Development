# coding:utf-8
import unittest
import time
from common.HTMLTestRunner_yo import HTMLTestRunner

discover1 = unittest.defaultTestLoader.discover("D:\\sele_project_t9\\case",
                                               "test_login*.py")


# 先打印出来，看有没加载
print(type(discover1))
discover2 = unittest.defaultTestLoader.discover("D:\\sele_project_t9\\case",
                                               "test_login*.py")

# all = unittest.TestSuite()
# for i in discover1:
#     all.addTests(i)
# for j in discover2:
#     all.addTests(j)
#
# print(all)




nowtime = time.strftime("%Y_%m_%d_%H_%M_%S")
print(nowtime)


reportpath = "D:\\sele_project_t9\\report"+"\\report%s.html"%nowtime

fp = open(reportpath, "wb")

runner = HTMLTestRunner(fp,
                        verbosity=2,
                        title="这是我的报告",
                        description="报告内容如下",
                        retry=1)
runner.run(discover1)