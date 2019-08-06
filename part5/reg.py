# -*- coding:utf-8 -*-
"""
正则表达式
记录文本规则的代码
时一个特殊的字符串
普通字符和元字符组成，其实就是对元字符的学习
"""
import re

reg_string = "hello2323hello@qq.com"
reg = "hello"
result = re.findall(reg, reg_string)
print(result)

# 元字符
'''
. 匹配除换行符以外的任意字符
\w 匹配字母或数字或下划线或汉字
\s 匹配任意的空白符
\d 匹配数字
\b 匹配单词的开始或结束
^ 匹配字符串的开始
$ 匹配字符串的结束

'''

# 查找以hello开头 后面那个hello就不出来了
reg = "^hello"
result = re.findall(reg, reg_string)
print(result)

'''
反义代码
\W 匹配任意不是字母的数字，下划线汉字的字符
\S 匹配任意不是空白符的字符
\D 匹配任意非数字
\B 匹配不是单词开头或结束的位置

'''

'''
限定符
* 重复零次或多次
+ 重复一次或多次
? 重复零次或一次
{n} 重复n次
{n,} 重复>=n次
{n,m} 重复n到m次
'''
reg = "\d{4}"
result = re.findall(reg, reg_string)
print(result)

reg = "[0-9a-z]{4}"
result = re.findall(reg, reg_string)
print(result)

print("match 匹配当前字符串以这个reg开头")
reg = "hello"
result = re.match(reg, reg_string)
print(result)

'''
匹配ip
'''
ip = "192.168.0.1;192.112.1.1"
reg = "\d{3}.\d+.\d+.\d+"
result = re.findall(reg, ip)
print(result)

reg="(\d{1,3}.){3}\d{1,3}"
result = re.search(reg, ip)[0]
print(result)


'''
组匹配
'''
str="phone:137633,postcode:514300"
reg="phone:(\d{6}),postcode:(\d{6})"

print(re.search(reg, str)[0])
print(re.search(reg, str)[1])
print(re.search(reg, str)[2])
print(re.search(reg, str).group(0))
print(re.search(reg, str).group(1))
print(re.search(reg, str).group(2))

