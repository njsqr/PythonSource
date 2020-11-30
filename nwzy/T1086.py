#!/user/bin/env python
# _*_ coding:utf-8 _*_

"""
题目描述: 对于输入的每个字符串，查找其中的最大字母，在该字母后面插入字符串“(max)”。
输入: 输入数据由一行长度不超过100的字符串组成，字符串仅由大小写字母构成。
输出: 对于每个测试实例输出一行字符串，输出的结果是插入字符串“(max)”后的结果，如果存在多个最大的字母，就在每一个最大字母后面都插入"(max)"。
样例输入
abcdefgfedcba
样例输出
abcdefg(max)fedcba
"""
str=input()
ch=max(str)
str=str.replace(ch,ch+'(max)')
print(str)