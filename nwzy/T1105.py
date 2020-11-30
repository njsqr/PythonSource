#!/user/bin/env python
# _*_ coding:utf-8 _*_

"""
题目描述: “回文串”是一个正读和反读都一样的字符串，比如“level”或者“noon”等等就是回文串。请写一个程序判断读入的字符串是否是“回文”。
输入: 输入是一个字符串
输出: 如果一个字符串是回文串，则输出"yes",否则输出"no".
样例输入
level
样例输出
yes
"""
str=input()
str_hui=str[::-1]
if str==str_hui:
    print('yes')
else:
    print('no')