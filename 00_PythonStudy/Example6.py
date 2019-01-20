# !/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Date: 2019/1/20 8:35
# @Author: Daniel_Zhao / YFDOOR
# @File: Example6.py
# @IDE: PyCharm
# 题目：暂停一秒输出，并格式化当前时间。
# 程序分析：无。

import time
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
time.sleep(1)
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
