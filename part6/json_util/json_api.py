# -*- coding:utf-8 -*-
import json

"""
dumps是将dict转化成str格式，loads是将str转化成dict格式。
dump和load也是类似的功能，只是与文件操作结合起来了。
"""
d = dict(name='思聪', age=29, score=80)
# 用json工具序列化为json字符串
str = json.dumps(d)
print(str)

f = open('dumpjson.txt', 'w')
json.dump(d, f)
f.close()

# 反序列化为字典
d2 = json.loads(str)
print(d2)

f2 = open('dumpjson.txt', 'r')
d3 = json.load(f2)
print(d3)
