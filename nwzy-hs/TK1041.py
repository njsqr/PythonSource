#!/usr/bin/env python
# encoding: utf-8
"""
@author: caopeng
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: TK1041.py
@time: 2019/9/19 16:51
@desc:

————————————————

题目描述
有一些数，想把这些数最后合成一个数，要求花费最小，操作如下：

每次在剩余的数中选择两个数，将这两个数相加放到剩余数中，原来的两个数消失，这种操作的花费是新生成的数的大小。

总花费就是所有这种操作的花费和，我们的目的是花费尽量小

输入格式
输入的第一行是一个整数C，表示有C个数。

接下来每行一个数，一共c行

输出格式
输出最小花费。

输入输出样例
样例 1
输入样例 复制

3
8
5
8
输出样例 复制

34

"""

c=int(input())
sum=0
listn=[]
for i in range(c):
    listn.append(int(input()))
while len(listn)>1:
    listn.sort()
    sum+=listn[0]+listn[1]
    listn.append(listn[0]+listn[1])
    listn.pop(0)
    listn.pop(0)
print(sum)