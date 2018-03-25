# coding:utf-8

# coding:utf-8
import unittest

class IntegerArithmeticTestCase(unittest.TestCase):
    u'''测试加减法集合'''
    def testAdd(self):  # test method names begin with 'test'
        u'''测试加法：1+1'''
        self.assertEqual((1 + 2), 4)
        self.assertEqual(0 + 1, 1)

    def testMultiply(self):
        u'''测试减法：2-1'''
        self.assertEqual((0 * 10), 0)