#!/user/bin/env python
# _*_ coding:utf-8 _*_

"""
题目描述: 输入一个十进制数N，将它转换成R进制数输出。
输入: 每个测试实例包含两个整数N(1<=N<=1e9)和R(2<=r<=16)
输出: 为每个测试实例输出转换后的数，每个输出占一行。如果R大于10，则对应的数字规则参考16进制（比如，10用A表示，等等）。
样例输入
7 2
样例输出
111
"""
n,r=map(int,input().split())
R=['A','B','C','D','E','F']
list=[]
while n!=0:
    list.append(n%r)
    n=n//r
list=list[::-1]
for i in range(len(list)):
    if int(list[i]) > 10:
        list[i]=R[int(list[i])-10]
    if i==len(list)-1:
        print(list[i])
    else:
        print(list[i],end='')