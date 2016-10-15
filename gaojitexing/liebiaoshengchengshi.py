# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 20:14:48 2016

@author: primer.sfc
运用列表生成式，可以快速生成list，可以通过一个list推导出另一个list，而代码却十分简洁。
"""
'''
#列表生成式
L=[x * x for x in range(1,11)]
print(L)
#加判断条件if
K=[x*x for x in range(1,11) if x%2 ==0 ]
print(K)

M=[m+n for m in 'Fuck' for n in'HJKL']
print(M)

import os
X=[d for d in os.listdir('.')]
print(X)

d ={'x':'D','y':'B','z':'C'}
X = [k + '=' + v for k,v in d.items()]
print(X)
'''
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x for x in L1 if isinstance(x,str)== True]
print(L2)      