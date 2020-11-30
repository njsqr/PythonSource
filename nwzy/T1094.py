#!/user/bin/env python
# _*_ coding:utf-8 _*_

"""
题目描述: 给定一段连续的整数，求出他们中所有偶数的平方和以及所有奇数的立方和。
输入: 输入数据包含一行，由两个整数m和n组成。
输出: 对于输入数据，输出一行，应包括两个整数x和y，分别表示该段连续的整数中所有偶数的平方和以及所有奇数的立方和。
样例输入
1 3
样例输出
4 28
"""
m,n=map(int,input().split())
sum1=0
sum2=0
for i in range(m,n+1):
    if i%2==0:
        sum1+=i**2
    else:
        sum2+=i**3
print(sum1,sum2)