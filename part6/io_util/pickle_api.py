# -*- coding:utf-8 -*-
# import pickle
# 为了保证2,3和谐

import pickle

"""序列化和反序列化"""
'''
序列化
'''

d = dict(name='思聪', age=29, score=80)
str = pickle.dumps(d)
print(str)

f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

'''
反序列化
'''

d2 = pickle.loads(str)
print(d2)

f2 = open('dump.txt', 'rb')
d3 = pickle.load(f2)
f2.close()
print(d3)
