#!/user/bin/env python
# _*_ coding:utf-8 _*_

"""
题目描述: 输入n(n<100)个数，找出其中最小的数，将它与最前面的数交换后输出这些数。
输入: 输入数据占一行，每行的开始是一个整数n，表示这个测试实例的数值的个数，跟着就是n个整数。
输出: 对于每组输入数据，输出交换后的数列，每组输出占一行。
样例输入
4 2 1 3 4
样例输出
1 2 3 4
"""

list=[int(x) for x in input().split()]
n=list.pop(0)
p=list.index(min(list))
list[0],list[p]=list[p],list[0]
for i in range(len(list)):
    if i==len(list)-1:
        print(list[i])
    else:
        print(list[i],end=' ')

