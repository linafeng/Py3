# -*- coding:utf-8 -*-
import threading
"""
线程局部变量可以放threading.local()
"""


local_school = threading.local()


def process_student():
    std = local_school.student
    print('Hello %s (%s)\n' % (std, threading.current_thread().name))


def process_thread(name):
    local_school.student = name
    process_student()


t1 = threading.Thread(target=process_thread, args=('Tom',), name='TA')
t2 = threading.Thread(target=process_thread, args=('Jack',), name='TB')
t3 = threading.Thread(target=process_thread, args=('JackC',), name='TC')
t3.start()
t1.start()
t2.start()

# t1.join()
# t2.join()
# t3.join()
