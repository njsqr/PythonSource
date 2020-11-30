"""
@author
题目描述: 给定n（是偶数）个数字，n不超过100，他们的输入编号从左到右是1,2,3,...n,
希望你交换他们次序输出，交换规则是编号1和2交换，编号3和4交换，依次类推编号n-1和n交换
输入: 第一行一个整数n
      第二行n个整数
输出: 输出交换后的结果
样例输入
4
1 2 3 4
样例输出
2 1 4 3
"""
n=int(input())
listn=[int(x) for x in input().split()]
for i in range(0,n,2):
    listn[i],listn[i+1]=listn[i+1],listn[i]
for x in listn:
    print(x,end=' ')

