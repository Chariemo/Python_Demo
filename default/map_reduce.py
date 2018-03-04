# -*- coding: utf-8 -*-

from functools import reduce

L1 = {'0':1, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}

def str2int(s):
    def func(x, y):
        return x * 10 + y
    def char2num(n):
        return L1[n];
    return reduce(func, map(char2num, s))

print(str2int('234') == 234)