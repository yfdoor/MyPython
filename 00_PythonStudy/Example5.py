#  Copyright (c) 2019. Daniel's python study project.
# 题目：暂停一秒输出。
# 程序分析：使用 time 模块的 sleep() 函数。
import time
MyD = {1: 'a', 2: 'b'}
for key, value in dict.items(MyD):
    print("%s: %s" % (key, value))
    time.sleep(1)
