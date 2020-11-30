#!/user/bin/env python
# _*_ coding:utf-8 _*_
"""
题目描述: 给定一个日期，输出这个日期是该年的第几天。
输入: 输入数据占一行，数据格式为YYYY/MM/DD组成，具体参见sample input ,另外，可以向你确保所有的输入数据是合法的。
输出: 对于输入数据，输出一行，表示该日期是该年的第几天。
样例输入
1985/1/20
样例输出
20
"""
import time

str=input()
t = time.strptime(str, "%Y/%m/%d")
print(t[7])
