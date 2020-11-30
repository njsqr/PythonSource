#!/user/bin/env python
# _*_ coding:utf-8 _*_

"""
题目描述: 输入一个百分制的成绩t，将其转换成对应的等级，具体转换规则如下：
90~100为A;
80~89为B;
70~79为C;
60~69为D;
0~59为E;
输入: 输入数据占一行，由一个整数组成。
输出: 对于输入数据，输出一行。如果输入数据不在0~100范围内，请输出一行：“Score is error!”。
样例输入
56
样例输出
E
"""
n=int(input())
if n in range(90,101):
    print('A')
elif n in range(80,90):
    print('B')
elif n in range(70,80):
    print('C')
elif n in range(60,70):
    print('D')
elif n in range(0,60):
    print('E')
else:
    print('Score is error!')