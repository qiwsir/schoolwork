# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 2020

@author: XinweiWen
"""

import random
n = random.randint(0,100)                                 #定义n为产生100以内的随机整数
i = 0                                                     #定义i为猜测的次数

while True:
    guess = int(input("不妨来猜一下100以内的整数："))       #定义guess来存储用户输入数字
    i += 1                                           #执行循环一次，i增加1，计数猜测次数
    if guess == n:
        print("太厉害了，猜对啦！")
        break
    if guess > 100.1 :                         #判断输入的是否为大于100的整数
        print('输入内容必须为小于100的整数！！！\n再猜一次吧！\n')
    elif guess > n:
        print("大了！继续猜，猜对有奖哦！")
    else:
        print("小了！继续猜，猜对有奖哦！")
  
print('\n你一共猜了'+str(i)+'次。猜对了也没奖，游戏结束！')



