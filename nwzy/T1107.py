#!/user/bin/env python
# _*_ coding:utf-8 _*_

"""
题目描述: 给定三条边，请你判断一下能不能组成一个三角形。
输入: 每行一个实例，包含三个正数A,B,C。
输出: 对于每个测试实例，如果三条边长A,B,C能组成三角形的话，输出YES，否则NO。
样例输入
1 2 3
样例输出
NO
"""
a,b,c=map(float,input().split())
if (a+b>c)&(a+c>b)&(b+c>a)&(abs(a-b)<c)&(abs(a-c)<b)&(abs(b-c)<a):
    print('YES')
else:
    print('NO')