# -*- coding:utf-8 -*-
""" 计算机"""
first_number = input('please input first num:')
operation = input('please input operation:')
second_number = input('please input second number:')
first_number = int(first_number)
second_number = int(second_number)
if operation == "+":
	result = first_number + second_number
	result = str(result)
	print("result is: " + result)
