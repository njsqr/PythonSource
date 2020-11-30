#!/user/bin/env python
# _*_ coding:utf-8 _*_

"""
题目描述: 对于给定的一个字符串，统计其中数字字符出现的次数。
输入: 输入数据有多行，第一行是一个整数n，表示测试实例的个数，后面跟着n行，每行包括一个由字母和数字组成的字符串。
输出: 对于每个测试实例，输出该串中数值的个数，每个输出占一行。
样例输入
1
asdfasdf123123asdfasdf
样例输出
6
"""

lists=[]
n=int(input())
for i in range(0,n):
    lists.append([input()])
for i in range(0,n):
    count = 0
    for ch in lists[i][0]:
        if ch.isdigit():
            count+=1
    print(count)


# oStr = input('请输入一串字符:')
#
# str_num = 0
# spac_num = 0
# figue_num = 0
#
# for strs in oStr:
#     if strs.isalpha():
#         str_num += 1
#     elif strs.isdigit():
#         figue_num += 1
#     elif strs == ' ':
#         spac_num += 1
#     else:
#         pass
# print('英文字母有：%d' % str_num)
# print('数字有：%d' % figue_num)
# print('空格有：%d' % spac_num)