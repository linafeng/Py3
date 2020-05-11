# -*- coding:utf-8 -*-
from multiprocessing import Process
import os

"""
windows创建子进程,multiprocessing可移植性更高，在linux也可以运行
"""


def run_proc(name, time):
    print('Run child process %s (%s)...' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test', 124,))
    p.start()
    p.join()
    print('End')
