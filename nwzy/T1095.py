#!/user/bin/env python
# _*_ coding:utf-8 _*_

"""
题目描述:  统计给定的n个数中，负数、零和正数的个数。
输入:  输入数据占一行，每行的第一个数是整数n（n<100），表示需要统计的数值的个数，然后是n个实数；
输出:  对于输入数据，输出一行a,b和c，分别表示给定的数据中负数、零和正数的个数。
样例输入
6 0 1 2 3 -1 0
样例输出
1 2 3
"""

list=[float(n) for n in input().split()]
list.pop(0)
hu=0
zero=0
zheng=0
for i in list:
    if i<0:
        hu+=1
    elif i>0:
        zheng+=1
    else:
        zero+=1
print(hu,zero,zheng)
