#!/usr/bin/env python
# encoding: utf-8
"""
@author: caopeng
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: TK1102 数列有序!.py
@time: 2019/9/25 9:04
@desc:

————————————————
题目：1102 数列有序!
题目描述     有n(n<=100)个整数，已经按照从小到大顺序排列好，现在另外给一个整数x，请将该数插入到序列中，并使新的序列仍然有序。
输入格式     输入数据包由两行组成，第一行是n和m，第二行是已经有序的n个数的数列。
输出格式     对于每个测试实例，输出插入新的元素后的数列。
输入输出样例
样例 1
输入样例 复制
3 3
1 2 4
输出样例 复制
1 2 3 4
"""

n, m = map(int, input().split())

lists = list(map(int, input().rstrip().split()))
lists.append(m)
lists = list(set(lists))
lists.sort()
for i in range(len(lists)):
    if i == len(lists) - 1:
        print(lists[i])
    else:
        print(lists[i], end=' ')
