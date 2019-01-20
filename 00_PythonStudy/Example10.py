# !/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Date: 2019/1/20 9:25
# @Author: Daniel_Zhao / YFDOOR
# @File: Example10.py
# @IDE: PyCharm
# 题目：文本颜色设置。

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print(bcolors.WARNING + "警告的颜色字体?" + bcolors.ENDC)
