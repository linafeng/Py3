import multiprocessing
import threading


def loop1(t):
    x = 0
    while True:
        x = x ^ 1
        print(t, x)


# i����������ѭ��
for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop1, args=(i,))
    t.start()
