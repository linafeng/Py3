# -*- coding:utf-8 -*-
"""条件控制"""
'''
1.比较运算符 == > <  >=  <= !=
字符比较大小的话是比较ascii码表大小
'''
print('a' < 'B')
print(ord('a'))
print(ord('B'))
print(chr(76))

'''
成员运算符
in
not in
'''

'''
逻辑运算符
and 
or 
not
'''
house_person = ['建国', '爱国', '卫国']
print('建国' in house_person and '爱国' in \
      house_person)

# 关于true和false的讨论
'''
False
True
False
'''
print(True and False)
print(True or False)
print(not True)
'''
0
1
False
'''
print(1 and 0)
print(1 or 0)
print(not 1)

'''
大于0的数代表true
0
2
False
'''
print(2 and 0)
print(2 or 0)
print(not 2)

# 身份运算符
'''
is判断地址，==判断值
is
is not
'''
'''
TRUE 
TRUE
493707488
493707488
493707520
'''
i = 1
j = 1
print(i == j)
print(i is j)
print(id(i))
print(id(j))
j = j + 1
print(id(j))
'''
False
True
55145608
55146312
'''
list_1 = [1, 2, 3]
list_2 = [1, 2, 3]
print(list_1 is list_2)
print(list_1 == list_2)
print(id(list_1))
print(id(list_2))

'''
了解运算符的优先级
'''
