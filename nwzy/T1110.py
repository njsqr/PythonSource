"""
题目描述: 给你连续的n个整数,  你的任务是找出最长的上升的子连续数组,( 子连续数组就是一个数组的某一个连续的一段,换句话说就是从原来的数组之中截取一段连续的数字作为新数组)  上升是严格递增的( 后面某一项一定大于前面某一项)
输入: 输入一个   n 代表接下来有n个整数. (1 ≤ n ≤ 105)
      接下来在输入n个整数.a1, a2, ..., an (1 ≤ ai ≤ 109).
输出: 输出一个整数代表答案
样例输入
5
1 7 2 11 15
样例输出
3
"""
n=int(input())
max_count=count=1
lists=[int(x) for x in input().split()]
for i in range(len(lists)-1):
    min=lists[i]
    if lists[i+1]<=min:
        if max_count<count:
            max_count=count
        count=1
    else:
        count+=1
if max_count<count:
    max_count = count
print(max_count)