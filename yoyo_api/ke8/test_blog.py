# coding:utf-8
import unittest

from ke8.blog_api import *


class Test_Blog(unittest.TestCase):

    def setUp(self):
        self.s = requests.session()

    def test_01(self):
        # 1.登录
        login(self.s)
        # 2发帖
        re_url = fatie(self.s)
        # 3获取postid
        postid = get_postid(re_url)
        # 4删帖
        re1 = delet_tie(self.s, postid)
        # 5.断言
        self.assertTrue(re1)

