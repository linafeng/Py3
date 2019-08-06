# -*- coding:utf-8 -*-
from homework import char_type_util

"""
加密同时包含中文和英文的字符串，标点符号不处理，需要解密
"""
message = input("please input your message >>>")
#message = "Hello,我叫蓝胖子"
result = ""
# 加密过程
ascii_list = []
for char in message:
	if char_type_util.is_other(char):
		ascii_list.append(char)
	else:
		ascii_list.append(str(ord(char)))
result = '|'.join(ascii_list)
print("加密后的结果是：" + result)

# 解密过程
index_list = result.split("|")
after_result = ""
# 遍历我的数组
for index in index_list:
	# 数组中的字符串转上int值
	value = ''
	try:
		int_index = int(index)
		after_result += chr(int_index)
	except ValueError as e:
		after_result += index
print("解密后的数据>>>>" + after_result)
