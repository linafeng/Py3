# -*- coding: utf-8 -*-
import functools

'''
方式一
'''
print(int('1000', base=2))
'''
方式二，自定义函数
'''


def int2(str, base=2):
    return int(str, base)


print(int2('1000'))

'''
方式三，偏函数
'''
int_2 = functools.partial(int, base=2)
print(int_2('1000'))
