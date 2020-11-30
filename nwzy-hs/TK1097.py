#!/usr/bin/env python
# encoding: utf-8
"""
@author: caopeng
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: TK1097.py
@time: 2019/9/24 15:39
@desc:

————————————————

题目：1097 素数判定
题目描述
对于表达式n^2+n+41，当n在（x,y）范围内取整数值时（包括x,y）(-39<=x<y<=50)，判定该表达式的值是否都为素数。

输入格式
输入数据占一行，由两个整数x，y组成

输出格式
对于每个给定范围内的取值，如果表达式的值都为素数，则输出"OK",否则请输出“Sorry”,每组输出占一行。

输入输出样例
样例 1
输入样例 复制

0 1
输出样例 复制

OK

"""
import math
x,y=map(int,input().split())
flag=0
for i in range(x,y+1):
    for j in range(2, int(math.sqrt(i**2+i+41))+1):
        if (i**2+i+41)% j==0:
            flag=1
            break
if flag:
    print("Sorry")
else:
    print("OK")
