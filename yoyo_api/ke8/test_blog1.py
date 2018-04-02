# coding:utf-8
import unittest

import requests
from ke8.blog_lei import Blog


class Test_Blog(unittest.TestCase):

    def setUp(self):
        self.s = requests.session()
        self.blog = Blog(self.s)

    def test_01(self):
        # 1.登
        self.blog.login()
        re_url = self.blog.fatie()
        postid = self.blog.get_postid(re_url)
        r = self.blog.delet_tie(postid)
        print(r)
        self.assertTrue(r)

