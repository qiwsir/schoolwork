# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 2020

@author: XinweiWen

subject:Fibonacci Sequence
（只输出数列前10个数）
"""


"""法1：循环语句"""
def fib_1(x):
    a, b = 0, 1
    for i in range(x):
        a, b = b, a + b
        print(a)
fib_1(10)



"""法2：生成器"""
def fib_2(x):
    c, d = 0, 1
    while x > 0:
        yield d             #使用生成器yield
        c, d = d, c + d
        x -= 1

for i in fib_2(10):         #调用函数返回值是一个生成器，使用for循环遍历取值
    print(i)
        


"""法3：迭代器"""    
class Fib_3(object):
    def __init__(self, x):     
        self.x = x         #得到斐波那契数列元素的个数
        self.n = 0         #计算斐波那契数列的次数，依次访问初始化self.n = 0到self.x = x区间的整型数
        self.e = 0         #定义斐波那契数列的第一个数
        self.f = 1         #定义斐波那契数列的第二个数
                     
    def __iter__(self):
        return self         #返回迭代器本身
    
    def __next__(self):
        if self.n < self.x:     #判断是否可以迭代
           self.e, self.f = self.f, self.e + self.f
           self.n += 1
           return self.e
        else:
            raise StopIteration      #没有元素了抛出异常
            
results = Fib_3(10)
for result in results:     #遍历results中的元素，打印出来
    print(result)
     
     

"""法4：矩阵"""
import numpy as np

def fib_4(x):
    for i in range(x):
        res = pow(np.mat([[1, 1],[1, 0]]), i) * np.mat([[1], [0]])      #定义一个变量res存储矩阵相乘的结果
        print(int(res[0,0]))      #所得res应为2*1矩阵，只输出第一个元素

fib_4(10)
        

        
"""法5：定义空列表"""
def fib_5(x):
    lst = []
    for i in range(x):
        if i == 0 or i == 1:
            lst.append(1)
        else:
            lst.append(lst[i-1] + lst[i-2])
    print(lst)

fib_5(10)
        
    