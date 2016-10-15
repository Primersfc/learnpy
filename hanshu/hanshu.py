# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 15:50:03 2016

@author: primer.sfc

import math

def quadratic(a,b,c):
    dat = b * b - 4 * a * c
    x1 =( -b + math.sqrt(dat))/2*a
    x2 =( -b - math.sqrt(dat))/2*a
    return x1,x2
def tongji(name,age,city='mianyang'):
    print('name',name)
    print('age',age)
    print('city',city)
    
def pfh(*number):
    sum = 0
    for n in number:
        sum = sum + n * n
    return sum
"""
def f1(a,b,c=0,*args,**kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)