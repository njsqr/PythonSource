"""
@author
题目描述: 小明最近迷上了化学，几乎天天在实验室做实验，但是很多实验生成的化学产物的相对分子质量令他很困惑，不知如何计算，请你编程帮他计算。
输入: 输入的第一行是一个正整数n，表示有n组测试数据。 接下来n行每行输入一个字符串，表示某个分子式，分子式中只包含大写字母和数字。
注意：输入数据只包含8种元素，而这8种元素的相对原子质量如下：H(1)，C(12)，N(14)，O(16)，F(19)，P(31)，S(32)，K(39)。
输出: 对于每组输入，输出相对分子质量。
样例输入
4
H2O
KOH
CH4
SO2
样例输出
18
56
16
64
"""

ys = {'H': 1, 'C': 12, 'N': 14, 'O': 16, 'F': 19, 'P': 31, 'S': 32, 'K': 39}
lists = []
n = int(input())
for i in range(n):
    s = 0
    strs = input()
    for j in range(len(strs)):
        if 'A' <= strs[j] <= 'Z':
            k = j + 1
            l = 0
            while k < len(strs):
                if ('0' <= strs[k] <= '9'):
                    l = l * 10 + int(strs[k])
                else:
                    break
                k += 1
            if l > 0:
                s += ys[strs[j]] * l
            else:
                s += ys[strs[j]]
    lists.append(s)
for x in lists:
    print(x)
