#!/usr/bin/env python
# encoding: utf-8
"""
@author: caopeng
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: TK1120 数字反转.py
@time: 2019/9/25 14:29
@desc:
题目：1120 数字反转
题目描述     给定一个整数，请将该数各个位上数字反转得到一个新数。新数也应满足整数的常见形式，即除非给定的原数为零，否则反转后得到的新数的最高位数字不应为零（参见样例2）。
输入格式     输入共 1 行，一个整数N。   -1,000,000,000 ≤ N≤ 1,000,000,000。
输出格式     输出共 1 行，一个整数，表示反转后的新数。
输入输出样例
样例 1
输入样例 复制
-380
输出样例 复制
-83

————————————————
"""
n = int(input())
flag = 0
if n < 0:
    flag = 1
st = str(abs(n))
n = int(st[::-1])
if flag:
    print(n * (-1))
else:
    print(n)
