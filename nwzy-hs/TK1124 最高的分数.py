#!/usr/bin/env python
# encoding: utf-8
"""
@author: caopeng
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: TK1124 最高的分数.py
@time: 2019/9/25 13:05
@desc:
题目：1124 最高的分数
题目描述
孙老师讲授的《计算概论》这门课期中考试刚刚结束，他想知道考试中取得的最高分数。因为人数比较多，他觉得这件事情交给计算机来做比较方便。你能帮孙老师解决这个问题吗？
输入格式   输入两行，第一行为整数n（1 <= n < 100），表示参加这次考试的人数.第二行是这n个学生的成绩，相邻两个数之间用单个空格隔开。所有成绩均为0到100之间的整数。
输出格式   输出一个整数，即最高的成绩。
输入输出样例
样例 1
输入样例 复制
5
85 78 90 99 60
输出样例 复制
99

————————————————
"""
n=int(input())
lists=list(map(int,input().split()))
print(max(lists))