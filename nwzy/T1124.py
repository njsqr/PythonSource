"""
@author
题目描述: 孙老师讲授的《计算概论》这门课期中考试刚刚结束，他想知道考试中取得的最高分数。因为人数比较多，他觉得这件事情交给计算机来做比较方便。你能帮孙老师解决这个问题吗？
输入: 输入两行，第一行为整数n（1 <= n < 100），表示参加这次考试的人数.第二行是这n个学生的成绩，相邻两个数之间用单个空格隔开。所有成绩均为0到100之间的整数。
输出: 输出一个整数，即最高的成绩。
样例输入
5
85 78 90 99 60
样例输出
99
"""
n=int(input())
max=0
scor=[int(x) for x in input().split()]
for x in scor:
    if x>max:
        max=x
print(max)