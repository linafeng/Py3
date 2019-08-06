# -*- coding:utf-8 -*-
import os
# nt代表windows
print(os.name)

# 环境变量
print(os.environ)

# 当前路径的绝对路径
print(os.path.abspath("."))


print(os.path.join("/s","ff"))

#os.mkdir("")新建
#os.rmdir("")删除

#得到文件名
#('D:\\lina\\document\\PycharmProjects\\Py3', 'part6\x0cile_directory')
dir="D:\lina\document\PycharmProjects\Py3\part6\output.txt"
print(os.path.split(dir))

# 得到文件扩展名
#('D:\\lina\\document\\PycharmProjects\\Py3\\part6\\output', '.txt')
print(os.path.splitext(dir))

