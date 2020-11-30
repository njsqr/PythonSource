#!/usr/bin/env python
# encoding: utf-8
"""
@author: caopeng
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: TK1117 买房子.py
@time: 2019/9/25 9:54
@desc:
题目：1117 买房子
题目描述    某程序员开始工作，年薪N万，他希望在中关村公馆买一套60平米的房子，现在价格是200万，假设房子价格以每年百分之K增长，并且该程序员未来年薪不变，且不吃不喝，不用交税，每年所得N万全都积攒起来，问第几年能够买下这套房子？（第一年年薪N万，房价200万）
输入格式    一行，包含两个正整数N（10 <= N <= 50）, K（1 <= K <= 20），中间用单个空格隔开。
输出格式    如果在第20年或者之前就能买下这套房子，则输出一个整数M，表示最早需要在第M年能买下，否则输出Impossible。
输入输出样例
样例 1
输入样例 复制
50 10
输出样例 复制
8
————————————————
"""
n,k=map(int,input().split())
fj=200
i=1
while fj>n*i and i<=20:
    fj*=1+k/100
    i+=1
if i>20:
    print("Impossible")
else:
    print(i)