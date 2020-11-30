#!/user/bin/env python
# _*_ coding:utf-8 _*_

# 1005、题目描述：已知长方形的长和宽，求该长方形的面积和周长
# 输入：长方形的长a，宽b
# 输出：长方形的面积和周长，一行输出，中间用空格区分

print("请输入长方形的长a，宽b以空格间隔：")
a,b=map(int,input().split())
print(a*b,2*(a+b))