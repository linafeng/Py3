# -*- coding:utf-8 -*-

# https://www.zdic.net/zd/zb/cc1/
# pip3 install requests
# http请求的库
import requests
# 正则匹配的库
import re

# 抓取到网页的源代码 post
html_result = requests.get("https://www.zdic.net/zd/zb/cc1/")
print(html_result.text)

# 书写正则表达式来获取网页源代码的所有汉字
reg = "href='/hans/(.*)' "
print(re.findall(reg, html_result.text))
# hans_list 当中就是包含了我们想要的2500个常用汉字
hans_list = re.findall(reg, html_result.text)
print(hans_list)

# 我要加密的字符串
input_message = "Hello,我来学院学习"
# 我要存储加密完成的字符串
result = ""
''''
加密规则：
    到hans_list中去寻找我输入的汉字，并将其位置取出来，
    作为加密后的编号，并且使用| 把这些组的数字分开
    例如： 我爱中国 加密为  29|30|12|24|
'''
for hans in input_message:
	for index, element in enumerate(hans_list):
		if hans == element:
			print(index)
			# print(element)
			result += str(index) + "|"
print("加密后的数据>>>>" + result)

# 这里使用
index_list = result.split("|")
# print(index_list)
# 移除数据后的空元素
index_list.remove("")
# print(index_list)

# 声明一个变量用来存放解密后的结果
response_result = ""

# 遍历我的数组
for index in index_list:
	# 数组中的字符串转上int值
	int_index = int(index)
	response_result += hans_list[int_index]
print("解密后的数据>>>>" + response_result)

'''
print(ord('我'))
自己写一个加密程序，能够加密的内容是英文和汉字，同时加密并且解密
就是说，一段话中既有中文又有英文，标点符号不用处理
加密规则，获取ASCii码数字，中间用|分割

扩展内容：自定义规则玩起来
预习内容：
下载neo4j数据库，并学会简单的cypher语句。什么版本都行
'''
