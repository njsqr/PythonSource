#!/usr/bin/env python
# encoding: utf-8
"""
@author: caopeng
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: TK1022.py
@time: 2019/9/19 15:11
@desc:

————————————————
题目描述  某市出租车计价规则如下：起步4公里10元，即使你的行程没超过4公里；接下来的4公里，每公里2元；之后每公里2.4元。行程的最后一段即使不到1公里，也当作1公里计费。
一个乘客可以根据行程公里数合理安排坐车方式来使自己的打车费最小。
例如，整个行程为16公里，乘客应该将行程分成长度相同的两部分，每部分花费18元，总共花费36元。如果坐出租车一次走完全程要花费37.2元。
现在给你整个行程的公里数，请你计算坐出租车的最小花费。
输入格式   输入包含多组测试数据。每组输入一个正整数n（n<10000000），表示整个行程的公里数。  当n=0时，输入结束。
输出格式   对于每组输入，输出最小花费。如果需要的话，保留一位小数。
输入输出样例
样例 1
输入样例 复制
3
9
16
0

输出样例 复制
10
20.4
36
"""
list=[]
while 1:
    n=int(input())
    sum=0
    if n==0:
        break
    elif n<=4:
        sum=10
    elif 4<n<=8:
        sum=10+(n-4)*2
    else:
        while n>=8:
            sum+=18
            n-=8
        if n<=4:
            sum+=2.4*n
        else:
            sum+=10+(n-4)*2
    list.append(sum)
for x in list:
    if x==int(x):
         print(int(x))
    else:
        print("%.1f"%x)