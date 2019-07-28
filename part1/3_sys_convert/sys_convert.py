# -*- coding:utf-8 -*-
"""运算符"""
'''
进制运算
'''
# 十进制转二进制 打印0b10000
i = 16
j = bin(i)
print(j)

# 十进制转8进制 0o20
j = oct(i)
print(j)

# 十进制转16进制 0x10
j = hex(i)
print(j)

# 二进制转十进制
k = '10'
j = int(k, 2)
print(j)

# 八进制转换十进制
j = int(k, 8)
print(j)

# 十六进制转十进制
j = int(k, 16)
print(j)
