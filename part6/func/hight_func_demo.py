# -*- coding:utf-8 -*-
"""
高阶函数
"""


def add(x, y, f):
    return f(x) + f(y)


print(add(-2, 5, abs))  # 7


def output_func(x, f):
    return f(x) * f(x)


def test(x):
    return x * 2 + 1;


print(output_func(5, test))  # (5*2+1)*(5*2+1)=11*11=121


