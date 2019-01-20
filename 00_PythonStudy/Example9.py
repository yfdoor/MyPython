# !/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Date: 2019/1/20 9:21
# @Author: Daniel_Zhao / YFDOOR
# @File: Example9.py
# @IDE: PyCharm

def Hello():
    print('Hello Daniel')


def Two_Hello():
    for i in range(3):
        Hello()


if __name__ == '__main__':
    Two_Hello()
