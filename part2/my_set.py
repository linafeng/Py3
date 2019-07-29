# -*- coding:utf-8 -*-
"""集合,set无序不重复 <class 'set'>"""
'''
两种声明方法
{}
set()
'''
# 声明一个集合
set_param = {'aa', 'bb', 'cc', 'aa'}
print(type(set_param))
print(set_param)

# 判断元素是否在集合内
print('cc' in set_param)
print('gg' in set_param)

# 集合间的运算
# 打印{'a', 'l'}
# {'a','b'}
a = set('lla')
b = set('bba')
print(a)
print(b)
# 同时包含的元素
print(a & b)
# a或b包含的元素
print(a | b)
# 不同时包含的元素
print(a ^ b)

# 集合添加元素
set_param = set(('vv', 'bm', 'p'))
print(set_param)

# 移除指定元素
set_param.remove('vv')
print(set_param)

# 随机移除一个元素
pop_param = set_param.pop()
print(pop_param)
print(set_param)

# 计算集合的个数
print(len(set_param))

# 清空集合 空的打印set()
set_param.clear()
print(set_param)
