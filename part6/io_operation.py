# -*- coding:utf-8 -*-
"""
读文件
read()将文本文件所有行读到一个字符串中
readline()是一行一行的读问，可以跳过指定行
readlines()是将文本文件中所有行独到一个list中，文本文件每一行是list一个元素

"""
'''
将文件"testio.txt"的内容写到"output.txt"中
'''
file = open("testio.txt")
# 'w'表示写权限默认为r读权限
file2 = open("output.txt", "w")
while True:
    line = file.readline()
    file2.write(line)
    if not line:
        break
file.close()
file2.close()

'''
文件迭代器用for循环的方法
'''
file3 = open("testio.txt")
file4 = open("output2.txt", "w")
for line in file3:
    file4.write(line)
file3.close()
file4.close()

'''
文件上下文管理
'''
# 打开文件
# 用with open自带关闭文本的功能
with open("testio.txt") as f:
    data = f.read()
    print(data)

# loop整个文章
with open("testio.txt") as f:
    for line in f:
        print("**" + line)

# 写入文本 write不带换行
with open("output3.txt", "w") as f:
    f.write("ff")
    f.write("ll")
# 打印ng并写入文件f中
with open("output4.txt", "w") as f:
    print("ng",file=f)


