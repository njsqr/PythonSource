#!/usr/bin/env python
# encoding: utf-8
"""
@author: caopeng
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: TK1101 字符串统计.py
@time: 2019/9/24 18:11
@desc:

————————————————
题目：1101 字符串统计
题目描述对于给定的一个字符串，统计其中数字字符出现的次数。
输入格式
输入数据有多行，第一行是一个整数n，表示测试实例的个数，后面跟着n行，每行包括一个由字母和数字组成的字符串。
输出格式
对于每个测试实例，输出该串中数值的个数，每个输出占一行。

输入输出样例
样例 1
输入样例 复制

1
asdfasdf123123asdfasdf
输出样例 复制
6
"""
n = int(input())  # 先输入一个数字代表需要输入几行，比如n=4，那么就需要再输入4行数据
q = []
for i in range(n):
    q.append(input())
for j in range(0, n):
    num = 0
    for k in range(len(q[j])):
        if "0" <= q[j][k] <= "9":
            num += 1
    print(num)
