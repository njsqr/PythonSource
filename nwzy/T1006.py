#!/user/bin/env python
# _*_ coding:utf-8 _*_

# 1006、题目描述：小E有一块手表，和普通的手表一样，从每天的00:00:00开始计时。
# 但奇怪的是，手表仅记录从开始计时过去的秒数，秒数在第二天的00:00:00清零。
# 现在给你小E的手表，你能告诉他现在的时间吗？
# 将时间以时:分:秒的形式输出（24小时制）
# 输入   S秒，0<=S<=86400
# 输出   h:m:s

flag=1
while(flag):
    S=int(input("请输入秒数0<=S<=86400 S："))
    if (0<=S<=86400):
        flag=0
    else:
        print("输入的数小于0或大于86400了！！！")

mins=divmod(S,60)
hours=divmod(mins[0],60)
print('现在时间为：%d : %d : %d'%(hours[0],hours[1],mins[1]))
