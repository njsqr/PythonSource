#!/usr/bin/env python
# encoding: utf-8
"""
@author: caopeng
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: TK1028.py
@time: 2019/9/19 17:48
@desc:

————————————————
题目描述
小C很喜欢倒着写单词，现在给你一行小C写的文本，你能把每个单词都反转并输出它们吗？

输入格式
输入包含多组测试样例。第一行为一个整数T，代表测试样例的数量，后面跟着T个测试样例。

每个测试样例占一行，包含多个单词。一行最多有1000个字符。

输出格式
对于每一个测试样例，你应该输出转换后的文本。

输入输出样例
样例 1
输入样例 复制

3
olleh !dlrow
I ekil .bulcmca
I evol .mca
输出样例 复制

hello world!
I like acmclub.
I love acm.


"""
listn=[]
T=int(input())
for i in range(T):
    listn.append([])
    listn[i].append(input().split())

print(listn[0][0])
print(listn[1][5];;)
# for i in range(T):
#     m=0
#     for j in range(len(listn[i])):
#         print(listn[i][j],end='  ')
#         if listn[i][j]==' 'or j==len(listn[i]):
#             for k in range(j-1,m-1,-1):
#                 print(listn[i][k])
#             if listn[i][j]!='\0':
#                 print(" ")
#                 m=j
#         print("\n")