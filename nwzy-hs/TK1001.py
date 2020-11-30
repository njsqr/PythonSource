#!/usr/bin/env python
# encoding: utf-8
"""
@author: caopeng
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: ${NAME}.py
@time: ${DATE} ${TIME}
@desc:

————————————————
"""
N = int(input())
list = []
# n = 0
# while (n < N):
#     a, b = map(int, input().split())
#     list.append(a + b)
#     n += 1
for i in range(0,N):
    a, b = map(int, input().split())
    list.append(a+b)
for x in list:
    print(x)
