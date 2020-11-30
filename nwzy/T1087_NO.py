#!/user/bin/env python
# _*_ coding:utf-8 _*_

"""
题目描述: 统计每个元音字母在字符串中出现的次数。
输入: 输入数据首先包括一个整数n，表示测试实例的个数，然后是n行长度不超过100的字符串。
输出: 对于每个测试实例输出5行，格式如下：
a:num1
e:num2
i:num3
o:num4
u:num5
样例输入
1
aeiou
样例输出
a:1
e:1
i:1
o:1
u:1
"""
n=int(input())
num1=num2=num3=num4=num5=0
str=[]
for i in range(0,n):
    str=input()
    num1+=str.count('a')
    num2+=str.count('e')
    num3+=str.count('i')
    num4+=str.count('o')
    num5+=str.count('u')
print('a:%d'%num1)
print('e:%d'%num2)
print('i:%d'%num3)
print('o:%d'%num4)
print('u:%d'%num5)