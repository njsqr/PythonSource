"""
@author
题目描述: 小蚂蚁童鞋最近迷上了日期，他想知道某一个年份是否是闰年，但是他不知道如何判断闰年，你能帮他程序实现吗？
给定一个年份，如果他是闰年，则输出"RUN!", 否则输出"NO RUN!"
输入: 输入一个年份
输出: 如果是闰年输出"RUN!",否则输出"NO RUN!"
样例输入
2016
样例输出
RUN!
"""
y=int(input())
if (y%400==0)|((y%4==0)&(y%100!=0)):
    print('RUN!')
else:
    print('NO RUN!')

