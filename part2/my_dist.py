# -*- coding:utf-8 -*-
"""字典 字典是一种可变容器类型，也是可以存储任意类型的对象"""

d = {'建国': 1, '爱国': 2}
print(d)

# 操作访问
print(d.keys())
print(d.values())
print(d['建国'])

# 增加
d['小米'] = 8
print(d)

# 更新
d['建国'] = 6
print(d)

# 删除
del d['小米']
print(d)

# 判断键是否在字典中
print('小米' in d)
print('建国' in d)

