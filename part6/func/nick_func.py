# -*- coding:utf-8 -*-
from functools import reduce

"""
匿名函数
python使用lambda创建匿名函数，函数体比def简单得多
他的主体只是一个表达式而不是代码块
"""
sum = lambda x, y: x + y
print(sum(1, 2))

# map
l = [1, 2, 3]
new_list = list(map(lambda i: i + 1, l))
map_obj = map(lambda i: i + 1, l)
print(map(lambda i: i + 1, l))

print(new_list)

# 两个数组搞成一个单独的数组
l2 = [4, 5, 6]
new_list2 = list(map(lambda x, y: x + y, l, l2))
print(new_list2)

# reduce 就是吧一个list缩成一个值，用在二院操作函数，先对集合中
# 的第1,2个数据进行操作，再用结果跟第三个数进行操作

l3 = [1, 2, 3, 4, 5]
print(reduce(lambda x, y: x + y, l3))  # 15

# 也可以给初始值
print(reduce(lambda x, y: x + y, l3, 10))  # 25

# filter
print(list(filter(lambda x: x >= 4, l3)))

