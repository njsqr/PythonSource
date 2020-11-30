#!/user/bin/env python
# _*_ coding:utf-8 _*_

# 1007、题目描述
# 给出两个数，判断两者的大小关系
# 输入   a,b两个数
# 输出
# 若a>b，输出"a>b"
# 若a<b，输出"a<b"
# 若a=b，输出"a==b"

print("请输入两个数a b以空格间隔：")
a,b=map(int,input().split())
if a>b:
    print('a > b')
elif a<b:
    print('a < b')
else:
    print('a == b')