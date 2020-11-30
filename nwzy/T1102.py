#!/user/bin/env python
# _*_ coding:utf-8 _*_
"""
题目描述: 有n(n<=100)个整数，已经按照从小到大顺序排列好，现在另外给一个整数x，请将该数插入到序列中，并使新的序列仍然有序。
输入: 输入数据包由两行组成，第一行是n和m，第二行是已经有序的n个数的数列。
输出: 对于每个测试实例，输出插入新的元素后的数列。
样例输入
3 3
1 2 4
样例输出
1 2 3 4
"""
n,m=map(int,input().split())
list=[int(x) for x in input().split()]
for i in list:
    if m<i:
        #list.index(i)
        list.insert(list.index(i),m)
        break
for i in range(len(list)):
    if i==len(list)-1:
        print(list[i])
    else:
        print(list[i],end=' ')
