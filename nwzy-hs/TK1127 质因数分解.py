#!/usr/bin/env python
# encoding: utf-8
"""
@author: caopeng
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: TK1127 质因数分解.py
@time: 2019/9/25 13:16
@desc:
题目：1127 质因数分解
题目描述    已知正整数 n 是两个不同的质数的乘积，试求出较大的那个质数。
输入格式    输入只有一行，包含一个正整数 n。
输出格式    输出只有一行，包含一个正整数 p，即较大的那个质数。
数据范围与提示
n<=10^8
输入输出样例
样例 1
输入样例 复制
21
输出样例 复制
7
————————————————
"""
import math
n=int(input())
for i in range(2,int(math.sqrt(n))+1):
    if n%i==0:
        print(int(n/i))
        break