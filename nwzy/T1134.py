"""
@author
题目描述: 小蚂蚁童鞋最近迷上了时间转换，他想知道某一个时刻转换为秒，一共是多少秒，他请教学编程的你帮他实现程序！
给定一个时间2:10:5，转化为秒数是7805（=2*3600+10*60+5）
输入: 输入一个时间
输出: 输出对应的秒数
样例输入
1:0:20
样例输出
3620
"""
h,m,s=map(int,input().split(':'))
print(h*3600+m*60+s)