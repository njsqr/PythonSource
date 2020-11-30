#!/user/bin/env python
# _*_ coding:utf-8 _*_

"""
题目描述: 假设一个班有n(n<=50)个学生，每人考m(m<=5)门课，求每个学生的平均成绩和每门课的平均成绩，并输出各科成绩均大于等于平均成绩的学生数量。
输入: 输入数据第一行包括两个整数n和m，分别表示学生数和课程数。然后是n行数据，每行包括m个整数（即：考试分数）。
输出: 对于每个测试实例，输出3行数据，第一行包含n个数据，表示n个学生的平均成绩，结果保留两位小数；第二行包含m个数据，表示m门课的平均成绩，
      结果保留两位小数；第三行是一个整数，表示该班级中各科成绩均大于等于平均成绩的学生数量。
样例输入
2 2
5 10
10 20
样例输出
7.50 15.00
7.50 15.00
1
"""
scoreTable=[]
countStudent=0
n,m=map(int,input().split())
for i in range(n):
    score=[int(x) for x in input().split()]
    studentScore = 0
    for y in score:
        studentScore+=y
    score.append(studentScore)
    scoreTable.append(score)
score=[]
for j in range(m):
    subjectScore=0
    for k in range(n):
        subjectScore+=scoreTable[k][j]
    score.append(subjectScore)
scoreTable.append(score)
for i in range(n):
    for j in range(m):
        if scoreTable[i][j]<scoreTable[n][j]/n :
            break
    else:
        countStudent+=1
for i in range(n):
    if i==n-1:
        print('%.2f'%(scoreTable[i][m]/m))
    else:
        print('%.2f'%(scoreTable[i][m]/m),end=' ')

for i in range(m):
    if i==m-1:
        print('%.2f'%(scoreTable[n][i]/n))
    else:
        print('%.2f'%(scoreTable[n][i]/n),end=' ')
print(countStudent)