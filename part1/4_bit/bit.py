# -*- coding:utf-8 -*-
# 按位与运算 &
i = 11
j = 2
z = i & j
print(bin(i))
print(bin(j))
print(bin(z))
print(z)

# 按位或运算 |
z = i | j
print(bin(i))
print(bin(j))
print(bin(z))
print(z)

# 按位异或运算 ^ 不同为1相同为0
z = i ^ j
print(bin(i))
print(bin(j))
print(bin(z))
print(z)

# 按位取反运算 ~
'''
11取反应该是-11-1=-12

'''
z = ~i
print(bin(i))
print(bin(z))
print(z)

# 左移运算符 << 右边(低位)补充2个零
q = 2;
print(bin(q))
z = q << 2
print(bin(z))

# 右移运算符 >> 右边(低位)去掉2位
q = 10
print(bin(q))
z = q >> 2
print(bin(z))
