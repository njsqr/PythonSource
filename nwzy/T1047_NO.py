"""
@author
题目描述: 给你两个集合，要求{A} + {B}。 注:同一个集合中不会有两个相同的元素。
输入: 每组输入数据分为三行，第一行有两个数字n，m(0<n，m<=10000)，分别表示集合A和集合B的元素个数。后两行分别表示集合A和集合B。
      每个元素为不超出int范围的整数，每个元素之间有一个空格隔开。
输出: 针对每组数据输出一行数据，表示合并后的集合，要求从小到大输出，每个元素之间有一个空格隔开。
样例输入
1 2
1
2 3
1 2
1
1 2
样例输出
1 2 3
1 2
"""

n1,m1=map(int,input().split())
listA1=[int(x) for x in input().split()]
listA2=[int(y) for y in input().split()]

n2,m2=map(int,input().split())
listB1=[int(x) for x in input().split()]
listB2=[int(y) for y in input().split()]

for x in listA2:
    if listA1.count(x)==0:
        listA1.append(x)
for x in listB2:
    if listB1.count(x)==0:
        listB1.append(x)
listA1.sort()
listB1.sort()
for i in range(len(listA1)):
    if i==len(listA1)-1:
        print(listA1[i])
    else:
        print(listA1[i],end=' ')
for j in range(len(listB1)):
    if  j==len(listB1)-1:
        print(listB1[j])
    else:
        print(listB1[j],end=' ')

