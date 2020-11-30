#!/user/bin/env python
# _*_ coding:utf-8 _*_

"""
题目描述: 给定一个正整数k(3≤k≤15),把所有k的方幂及所有有限个互不相等的k的方幂之和构成一个递增的序列，例如，当k=3时，这个序列是：

1，3，4，9，10，12，13，…

（该序列实际上就是：3^0，3^1，3^0+3^1，3^2，3^0+3^2，3^1+3^2，3^0+3^1+3^2，…）

请你求出这个序列的第N项的值（用10进制数表示）。
可以认为是比特位依次为01，10，11，100，101，110...而最终的N也就是一串01序列，只需要对应位为一的幂值相加也就是最终结果了，代码大大简化

例如，对于k=3，N=100，正确答案应该是981。

输入: 输入文件sequence.in 只有1行，为2个正整数，用一个空格隔开：
k N  （k、N的含义与上述的问题描述一致，且3≤k≤15，10≤N≤1000）。
输出: 输出文件sequence.out 为计算结果，是一个正整数（在所有的测试数据中，结果均不超过2.1*109）。（整数前不要有空格和其他符号）。
样例输入
3 100
样例输出
981
"""
with open('sequence.in', 'r') as file:
    lists = file.readline().strip().split()
    kn = [int(x) for x in lists]
sum = 0
strs = bin(kn[1])[2:][::-1]
for i in range(len(strs)):
    if strs[i] != '0':
        sum += kn[0] ** i

with open('sequence.out', 'w') as f:
    f.write(str(sum)+'\n')

# with open('sequence.in','r') as file:
#     for line in file.readlines()[0:2]:
#         list=line.strip().split()
#         # listline=list.split()
#         k=[int(x) for x in list]
#         # list=line.split()
#         print(k[1],)
