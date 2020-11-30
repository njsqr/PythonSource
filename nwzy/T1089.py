#!/user/bin/env python
# _*_ coding:utf-8 _*_

"""
题目描述: 输入两点坐标（X1,Y1）,（X2,Y2）,计算并输出两点间的距离。
输入: 输入数据占一行，由4个实数组成，分别表示x1,y1,x2,y2,数据之间用空格隔开。
输出: 对于输入数据，输出一行，结果保留两位小数。
样例输入
0 0 0 1
样例输出
1.00
"""
from math import sqrt

x1,y1,x2,y2=map(float,input().split())
print('%.2f'%sqrt((x1-x2)**2+(y1-y2)**2))