#!/user/bin/env python
# _*_ coding:utf-8 _*_

# 题目描述:给出三个数a,b,c,若满足条件a<b<c，输出”Yes“，否则输出"No"
# 输入: 0<=a,b,c<=100
# 输出: Yes或者No
# 样例输入：1 3 8
# 样例输出：Yes

print("请输入两个数a b，c以空格间隔：")
a,b,c=map(int,input().split())
if a in range(0,10):
    if b in range(0,10):
        if c in range(0,10):
            if a<b<c:
                print('Yes')
            else:
                print('No')
