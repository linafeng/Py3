# -*- coding:utf-8 -*-
"""二进制文件的读取"""
'''
需要读取二进制流权限为rb 写则为wb
'''
file = open("pic1.jpg", "rb")
file2 = open("pic2.jpg", "wb")
file2.write(file.read())
file.close()
file2.close()
