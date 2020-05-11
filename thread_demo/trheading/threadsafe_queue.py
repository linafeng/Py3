# -*- coding:utf-8 -*-
# 线程队列
# FIFO: First in first out
# LIFO: Last in first out
# Priority Queue

import queue
import threading

# 先进先出的Queue
q = queue.Queue()
for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get())

# 先进后出的LifoQueue
q = queue.LifoQueue()
for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get())


class Task:
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description

    def __lt__(self, other):  # Python 2.7, implement __cmp__
        return self.priority < other.priority


# 优先级队列
q = queue.PriorityQueue()
q.put(Task(1, 'Important task'))
q.put(Task(10, 'Normal task'))
q.put(Task(100, 'Lazy task'))


def job(q):
    while True:
        task = q.get()
        print('Task: %s\n' % task.description)
        q.task_done()


threads = [threading.Thread(target=job, args=(q,)), threading.Thread(target=job, args=(q,))]
for t in threads:
    t.setDaemon(True)
    t.start()
q.join()
