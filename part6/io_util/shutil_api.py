# -*- coding:utf-8 -*-
import os
import shutil

'''
shutil
'''

# 拷贝文件
# shutil.copy('filea','fileb')
# 列出当前目录下的所有目录
print([x for x in os.listdir('.') if os.path.isdir(x)])
# 只想列出.py文件
print([y for y in os.listdir('.') if os.path.isfile(y) \
       and os.path.splitext(y)[1] == '.py'])
