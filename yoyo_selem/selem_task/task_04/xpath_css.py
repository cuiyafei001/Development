#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
web自动化作业悠悠我心 昨天 星期五 22:30
第4课作业：
1.写出10种不同的xpath定位语法，并备注每种定位的思路
2.写出5种不同的css定位语法，并备注每种定位的思路
"""
from selenium import webdriver
import time
# Firefox配置文件地址
path = r"C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\nwi4vflo.default"
proffile = webdriver.FirefoxProfile(path)
driver = webdriver.Firefox(proffile)

driver.get("http://www.cnblogs.com/cyfyywfc/")
# xpath定位
"""
1、 .//*[@id="blog_nav_myhome"]  id定位
2、 .//*[@name='wd']             name定位
3、 .//*[@class='mnav']          class定位
4、 .//*[text()="文章"]          text定位
5、 .//*[@type="text"]           type值定位
6、 .//*[@id='blog_nav_newpost' and @class='menu']  id and class组合定位
7、 .//a[contains(text(),'管')]  text模糊匹配定位
8、 .//input[@id='su']           标签id定位
9、 .//*[@id='nr']/option[1]     id定位通过索引找到目标
10、.//*[@id='blog_nav_newpost']/../../.. 通过id找到他爷爷元素
11、.//*[@id='u_sp']/a[3]        定位父级元素id，通过索引找到子元素
"""
# css定位
"""
1、#blog_nav_newpost             id定位
2、.menu                         class定位
3、.lavalamp-item>a              上级标签定位到class
4、[type='text/css']             type定位
5、input                         标签定位
6、[name='word']                 name定位
"""
