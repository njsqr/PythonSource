#!/usr/bin/env python
# encoding: utf-8
"""
@author: caopeng
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: TK1106 进制转换.py
@time: 2019/9/25 13:58
@desc:
题目：1106 进制转换
题目描述      输入一个十进制数N，将它转换成R进制数输出。
输入格式      每个测试实例包含两个整数N(1<=N<=1e^9)和R(2<=r<=16)
输出格式      为每个测试实例输出转换后的数，每个输出占一行。如果R大于10，则对应的数字规则参考16进制（比如，10用A表示，等等）。
数据范围与提示
输入输出样例
样例 1
输入样例 复制
7 2
输出样例 复制
111

————————————————
"""
# base = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F]
base = [str(x) for x in range(10)] + [chr(x) for x in range(ord('A'), ord('A') + 6)]
n, r = map(int, input().split())
num = n
lists = []
while True:
    if num == 0:
        break
    num, rem = divmod(num, r)
    lists.append(base[rem])
print(''.join([str(x) for x in lists[::-1]]))
