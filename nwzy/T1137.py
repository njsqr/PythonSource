"""
@author
题目描述: 给出n个数，最少增加多少可以使得每个数都相等？
输入: 第一行为n，第二行为n个数。
输出: 输出一个数，表示最少可以增加的值，使得每个数都相等。
样例输入
5
0 1 2 3 4
样例输出
10
"""
sum=0
n=int(input())
lists=[int(x) for x in input().split()]
max=max(lists)
for x in lists:
    sum+=max-x
print(sum)