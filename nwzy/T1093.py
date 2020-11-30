#!/user/bin/env python
# _*_ coding:utf-8 _*_

"""
题目描述: 给你n个整数，求他们中所有奇数的乘积。
输入: 输入数据占一行，每行的第一个数为n，表示本组数据一共有n个，接着是n个整数，你可以假设每组数据必定至少存在一个奇数。
输出: 输出每组数中的所有奇数的乘积，对于测试实例，输出一行。
样例输入
3 1 2 3
样例输出
3
"""
list=[int(n) for n in input().split()]
n=list.pop(0)
product=1
for i in list:
    if i%2!=0:
        product*=i
print(product)
