#!/user/bin/env python
# _*_ coding:utf-8 _*_

# 题目描述:给出三个整数，按照从小到大的顺序排列输出
# 输入:三个整数a,b,c
# 输出:按照从小到大的顺序输出三个数，输出在一行中
# 样例输入
# 3 8 1
# 样例输出
# 1 3 8

print("请输入两个数a b，c以空格间隔：")
a,b,c=map(int,input().split())
if a>b:
    a,b=b,a
if b>c:
    b,c=c,b
if  a>b:
    a,b=b,a
print(a,b,c)
