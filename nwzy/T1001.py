#!/user/bin/env python
# _*_ coding:utf-8 _*_

# 1001、题目描述：你的任务是计算a+b。
# 输入：第一行是一个整数N，表示后面会有N行a和b，通过空格隔开。
# 输出：对于输入的每对a和b，你需要在相应的行输出a、b的和。
# 如第二对a和b，对应的和也输出在第二行。

N=int(input("请输入整数N："))
n=0
while(n<N):
    print("请输入第 ",n+1," 组两个数a b以空格间隔：")
    a,b=map(int,input().split())
    print("这两个数的和为：",a+b)
    n+=1