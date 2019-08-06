# -*- coding:utf-8 -*-


# 判断是否为中文汉字
def is_chinese(unknown_char):
	if '\u4e00' <= unknown_char <= '\u9fa5':
		return True
	else:
		return False


# 判断是否为英文字母
def is_alphabet(unknown_char):
	if ('\u0041' <= unknown_char <= '\u005a') or ('\u0061' <= unknown_char <= '\u007a'):
		return True
	else:
		return False


# 判断是否为数字
def is_number(unknown_char):
	if '\u0030' <= unknown_char <= '\u0039':
		return True
	else:
		return False


# 其它语言符号或标点
def is_other(unknown_char):
	if not (is_chinese(unknown_char) or is_number(unknown_char) or is_alphabet(unknown_char)):
		return True
	else:
		return False
