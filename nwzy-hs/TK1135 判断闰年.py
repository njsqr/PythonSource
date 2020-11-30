#!/usr/bin/env python
# encoding: utf-8
"""
@author: caopeng
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: TK1135 判断闰年.py
@time: 2019/9/25 15:01
@desc:
题目：1135 判断闰年
题目描述    小蚂蚁童鞋最近迷上了日期，他想知道某一个年份是否是闰年，但是他不知道如何判断闰年，你能帮他程序实现吗？
            给定一个年份，如果他是闰年，则输出"RUN!", 否则输出"NO RUN!"
输入格式    输入一个年份
输出格式    如果是闰年输出"RUN!",否则输出"NO RUN!"
输入输出样例
样例 1
输入样例 复制
2016
输出样例 复制
RUN!
————————————————
"""
n = int(input())
if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
    print("RUN!")
else:
    print("NO RUN!")
