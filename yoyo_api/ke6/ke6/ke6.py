# coding:utf-8
import unittest

class IntegerArithmeticTestCase(unittest.TestCase):

    def testAdd(self):  # test method names begin with 'test'
        a = "aaa"
        b = "aaa"
        c = "aaaccc"
        self.assertTrue(a == b)  # pass
        self.assertEqual(a, b)  # pass
        # self.assertIn(c, a)     # Fail
        print("11111111")
        self.assertIn(a, c)     # pass
        self.assertTrue(a in c)
        self.assertFalse(a == c)

    def testMultiply(self):
        self.assertEqual((0 * 10), 0)
        self.assertEqual((5 * 8), 40)

if __name__ == '__main__':
    unittest.main()


