#!/usr/bin/env python
# encoding: utf-8
"""
@author: caopeng
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: TK1126 数字统计.py
@time: 2019/9/25 12:55
@desc:
题目：1126 数字统计
题目描述    请统计某个给定范围L, R的所有整数中，数字2出现的次数。
           比如给定范围2, 22，数字2在数2中出现了1次，在数12中出现1次，在数20中出现1次，在数21中出现1次，在数22中出现2次，所以数字2在该范围内一共出现了6次。
输入格式   输入共 1 行，为两个正整数 L 和 R，之间用一个空格隔开。
输出格式    输出共 1 行，表示数字 2 出现的次数。
输入输出样例
样例 1
输入样例 复制
2 22
输出样例 复制
6
————————————————
"""
l, r = map(int, input().split())
n = 0
for i in range(l, r + 1):
    st = str(i)
    for j in range(0, len(st)):
        if st[j] == '2':
            n += 1
print(n)
