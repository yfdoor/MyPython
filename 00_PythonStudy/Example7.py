# !/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Date: 2019/1/20 8:39
# @Author: Daniel_Zhao / YFDOOR
# @File: Example7.py
# @IDE: PyCharm
# 题目：输出指定格式的日期。
# 程序分析：使用 datetime 模块。

import datetime

print(datetime.date.today().strftime('%d/%m/%Y'))

ZXD = datetime.date(2013, 5, 31)
print(ZXD.strftime('%Y-%m-%d'))
zxd = ZXD + datetime.timedelta(days=10)
print(zxd.strftime('%Y-%m-%d'))
zxd = zxd.replace(year=zxd.year + 1)
print(zxd.strftime('%Y-%m-%d'))
