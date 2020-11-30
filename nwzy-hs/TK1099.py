#!/usr/bin/env python
# encoding: utf-8
"""
@author: caopeng
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: TK1099.py
@time: 2019/9/24 17:44
@desc:

————————————————
题目：1099 青年歌手大奖赛_评委会打分
题目描述
青年歌手大奖赛中，评委会给参赛选手打分。选手得分规则为去掉一个最高分和一个最低分，然后计算平均得分，请编程输出某选手的得分。

输入格式
输入数据占一行，每行的第一个数是n(2<n<=100)，表示评委的人数，然后是n个评委的打分。

输出格式
对于每组输入数据，输出选手的得分，结果保留2位小数，每组输出占一行。

输入输出样例
样例 1
输入样例 复制

3 99 98 97
输出样例 复制

98.00
"""

lists=list(map(int,input().split()))
n=lists[0]
lists.pop(0)
tot=0
for x in lists:
    tot+=x
avg=(tot-min(lists)-max(lists))/(n-2)
print("%.2f"%avg)