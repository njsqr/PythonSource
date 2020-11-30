"""
@author
题目描述: 网上流传一句话:"常在网上飘啊，哪能不挨刀啊～"。其实要想能安安心心地上网其实也不难，学点安全知识就可以。
首先，我们就要设置一个安全的密码。那什么样的密码才叫安全的呢？一般来说一个比较安全的密码至少应该满足下面两个条件：
(1).密码长度大于等于8，且不要超过16。
(2).密码中的字符应该来自下面“字符类别”中四组中的至少三组。这四个字符类别分别为：
1.大写字母：A,B,C...Z;
2.小写字母：a,b,c...z;
3.数字：0,1,2...9;
4.特殊符号：~,!,@,#,$,%,^;
给你一个密码，你的任务就是判断它是不是一个安全的密码。
输入: 每行一个密码（长度最大可能为50），密码仅包括上面的四类字符。
输出: 对于每个测试实例，判断这个密码是不是一个安全的密码，是的话输出YES，否则输出NO。
样例输入
a1b2c3d4
样例输出
NO
"""
specialCharacter=['~','!','@','#','$','%','^']
str=input()
count=flag_A=flag_a=flag_0=flag_spe=0
if 8<=len(str)<=16:
    for ch in str:
        if 'A'<=ch<='Z':
            flag_A=1
            continue
        if 'a'<=ch<='z':
            flag_a=1
            continue
        if '0'<=ch<='9':
            flag_0=1
            continue
        if specialCharacter.count(ch)>0:
            flag_spe=1
            continue
    count=flag_A+flag_a+flag_0+flag_spe
if count>=3:
    print('YES')
else:
    print('NO')


