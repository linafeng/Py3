import time
import threadpool


def long_op(n):
    print('%d\n' % n)
    time.sleep(2)


# 开辟指定数量的线程池
pool = threadpool.ThreadPool(2)
# 创建任务
tasks = threadpool.makeRequests(long_op, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(len(tasks))
# 执行
[pool.putRequest(task) for task in tasks]
pool.wait()
