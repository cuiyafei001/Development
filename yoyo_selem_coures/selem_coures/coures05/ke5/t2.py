# coding:utf-8
import unittest
# help(unittest)
class IntegerArithmeticTestCase(unittest.TestCase):

    def testAdd(self):  # test method names begin with 'test'
        # 所以的测试用例都要test开头
        self.assertEqual((1 + 2), 3)
        self.assertEqual(0 + 1, 3)   # 一个测试用例里面可以有多个断言

    def testMultiply(self):

        self.assertEqual((0 * 10), 0)
        self.assertEqual((5 * 8), 40)

if __name__ == '__main__':
    unittest.main()