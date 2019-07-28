# -*- coding:utf-8 -*-
"""声明字符串"""
# 单引号声明
s = 'gg'
print(s)
# 双引号声明
s = "ll"
print(s)
# 三引号声明 有格式
s = """hello

jj

"""
print(s)

# 字符串的操作
# 单个访问字符串中的字符
s = "world fff"
print(s[4])
# 访问字符串中的子串 切片操作
# 访问字符串的切片操作左闭右开原则
print('切片'+s[1:3])
#字符串的更新操作
print("Hello fiona"[:6]+"lina")

# 字符串的内建函数
# 查找字符串
s = "hello fiona".find("llo")
print(s)

#转换小写
print("dFF".lower())
#转换大写
print("dFF".upper())

#返回字符串的自然长度 以下打印6
print("qwe io".__len__())

# 判断字符串是否只包含空格
print(" ".isspace())
print("g ".isspace())


# 字符串替换
print("Hello fiona".replace("o","jd"))



# 字符串的成员运算
# 包含运算
s1 = "Hello fiona"
s2 = "a"
# 包含 in
print(s2 in s1)
# 不包含 not in
print(s2 not in s1)

# 转义字符 \
'''
\n是换行符
\t是tab制表符
\r是回车 光标到首航，打印\r之后的内容
'''
print('\"')
print("vvv\nkkk")
print("-----------")
print("ggg\rlll")

#输出原始字符串
print(r'hhhhh\nkkk')
print(R'hhhhh\nkkk')

#字符串的格式化输出
print('hello %s,%dperson'%('lina',2))
