#!/usr/bin/env python

# -*- coding: UTF-8 -*-

# 求1到99的和
if __name__ == "__main__":
    # 这是注释
    sum = 0    
    for index in range(1, 100):      # 这也是注释
        sum = sum + index
    
    print("1-99的和为: %d" % sum)