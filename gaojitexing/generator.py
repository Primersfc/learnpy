# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 20:38:18 2016

@author: primer.sfc

#容器和列表生成式的区别[] 和（）
L = [x * x for x in range(10)]
print(L)
g = (x * x for x in range(10))
print(g)
for n in g:
    print(n)

def fib(max):
    n,a,b = 0,0,1
    while n<max:
        print(b)
        a,b = b, a + b
        n=n+1
    return 'done'
fib(6)

def fib(max):
    n,a,b = 0,0,1
    while n<max:
        yield b#定义generator的另一种方法
        a,b = b, a + b
        n=n+1
    return 'done'
for n in fib(6):
    print(n)
"""
#打印杨辉三角
def triangles():
    L = [1]
    while True:
        yield L
        L.append(0)
        L= [L[i-1]+L[i] for i in range(len(L))]
n = 0
for x in triangles():
    print(x)
    n=n+1;
    if n>=10:
        break

#generator函数的“调用”实际返回一个generator对象：
    