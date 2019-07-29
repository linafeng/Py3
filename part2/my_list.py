# -*- coding:utf-8 -*-
"""列表 <class 'list'>"""
# 声明列表
list1 = []
print(type(list1))

list2 = ['ff', 13, 'fl', 14]
print(type(list2))

# 访问列表
print(list2[0])
print(list2[1:])
print(list2[1:3])

# 更新
list2[1] = '4i'
print(list2)

# 添加操作
list2.append('haha')
print(list2)

list2 = list2 + ['v', 4]
print(list2)



# 嵌套列表
list3 = [['ll', 3], [7, 8]]
print(list3[1])
print(list3[1][1])

# 返回列表的元素个数
print(len(list3))

# 删除操作
del list2[0]
print(list2)

# 移除列表中的元素,并且返回这个值
#del remove pop对比
print(list2)
val = list2.pop(1)
print(val)
print(list2)
list2.remove('v')
print(list2)

# 对列表中的元素进行排序
list4 = [1, 4, 7, 2, 3]
list4.sort()
print(list4)

# 查找列表中第一个匹配的元素的
print(list4.index(2))

'''

'''