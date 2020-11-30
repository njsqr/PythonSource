#!/usr/bin/env python
# encoding: utf-8
"""
@author: caopeng
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: TK1118 菲波那契数列.py
@time: 2019/9/25 9:47
@desc:
题目：1118 菲波那契数列
题目描述    菲波那契数列是指这样的数列: 数列的第一个和第二个数都为1，接下来每个数都等于前面2个数之和。
            给出一个正整数k，要求菲波那契数列中第k个数是多少。
输入格式    输入一行，包含一个正整数k。（1 <= k <= 46）
输出格式    输出一行，包含一个正整数，表示菲波那契数列中第k个数的大小
输入输出样例
样例 1
输入样例 复制
4
输出样例 复制
3

————————————————
"""
k=int(input())
a=1
b=1
if k==1 or k==2 :
    fn=1
else:
    for i in range(3,k+1):
        a,b=b,a+b
    fn=b
print(fn)