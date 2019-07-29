# -*- coding:utf-8 -*-
"""
正则表达式
记录文本规则的代码
时一个特殊的字符串
普通字符和元字符组成，其实就是对元字符的学习
"""
import re
reg_string = "hello2323hello@qq.com"
reg="hello"
result=re.findall(reg,reg_string)
print(result)

# 元字符
