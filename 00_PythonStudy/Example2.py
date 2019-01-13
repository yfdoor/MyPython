#  Copyright (c) 2019. Daniel's python study project.
# 题目：输入某年某月某日，判断这一天是这一年的第几天？
# 程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：

year = int(input('Year:\n'))
month = int(input('Month:\n'))
day = int(input('Day:\n'))
months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
if 0 < month <= 12:
    sum = months[month - 1]
else:
    print('Out of Month')
sum += day

leap = 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap = 1

if (leap == 1) and (month > 2):
    sum += 1

print('It is the %dth day' % sum)
