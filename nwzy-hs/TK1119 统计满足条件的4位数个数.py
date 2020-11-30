#!/usr/bin/env python
# encoding: utf-8
"""
@author: caopeng
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: TK1119 统计满足条件的4位数个数.py
@time: 2019/9/25 14:15
@desc:

————————————————
题目：1119 统计满足条件的4位数个数
题目描述     给定若干个四位数，求出其中满足以下条件的数的个数：
             个位数上的数字减去千位数上的数字，再减去百位数上的数字， 再减去十位数上的数字的结果大于零。
输入格式     输入为两行，第一行为四位数的个数n，第二行为n个的四位数，数与数之间以一个空格分开。(n <= 100)
输出格式     输出为一行，包含一个整数，表示满足条件的四位数的个数。
输入输出样例
样例 1
输入样例 复制
3
1113 1103 7019
输出样例 复制
2
"""
n =int(input())
# lists=list(map(int,input().rstrip().split()))
lists=input().split()
count=0
for x in lists:
    if eval(x[0])+eval(x[1])+eval(x[2])<eval(x[3]):
        count+=1
print(count)