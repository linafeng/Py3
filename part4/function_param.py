# -*- coding:utf-8 -*-
"""函数定义的格式"""


def my_func():
    print('my func')


def my_func_with_param(p1, p2):
    print(p1, p2)


my_func_with_param(1, 2)
# my_func_with_param(1)

# 关键字参数
my_func_with_param(p1=1, p2=2)


# 默认参数 如果调用者没有传值，那么就用默认值，可以不指定名字
# 混合使用时，非默认参数必须在默认参数的前边
def my_function_with_param(name, sex, age=15):
    print(name + ":" + str(age))


my_function_with_param('bb', 'M')
my_function_with_param('bb', 'M', age=2)


# 函数返回值
def my_func_return():
    return 1


p = my_func_return()
print(type(p))
print(p)


# 多个返回值
def func_with_return(name, age):
    return name, age


# result xiaoming 14
n, a = func_with_return('xiaoming', 14)
print(n, a)
# result元组 ('xiaoming', 14)
q = func_with_return('xiaoming', 14)
print(q)
print(type(q))


# 返回一个函数
def local_func(y):
    return y+1


def func_with_return_func(x):
    if x == 2:
        def inner_func(y):
            y * y
    if x == 3:
        def inner_func(y):
            return y * y * y
    return local_func


calc = func_with_return_func(4)
print(calc(4))
