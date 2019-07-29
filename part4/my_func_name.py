# -*- coding:utf-8 -*-
"""
__name__
只有子本模块启动时，__name__变量等于__main__
1.可以作为入口函数叫main函数
2.可以作为调试使用，原因是在其他模块调用本模块时，
__name__=main，if不会执行
"""


def my_print():
    print(__name__)


if __name__ == "__main__":
    my_print()
    print(1)
    print(__name__)
