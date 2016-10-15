# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 19:55:46 2016

@author: primer.sfc
"""
#字典迭代
d={'a':1,'b':2,'c':3}
for key in d:
    print(key)
for value in d.values():
    print(value)
for k,v in d.items():
    print(k,v)
    
for ch in 'ASDW':
    print(ch)
    
#判断一个对象是否迭代
from collections import Iterable
print(isinstance('abc',Iterable))#str
print(isinstance([1,2,3],Iterable))#list
print(isinstance(123,Iterable))#整数

#下标循环
for i,value in enumerate(['A','B','F']):
    print(i,value)
    
for x,y in[(1,1),(2,4),(3,9)]:
    print(x,y)
 