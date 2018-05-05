
# 顺序执行的单线程
'''
from threading import Thread
import time

def my_counter():
    i = 0
    for _ in range(100000000):
        i = i + 1
    return True

def main():
    thread_array = {}
    start_time = time.time()
    for tid in range(2):
        t = Thread(target=my_counter)
        t.start()
        t.join()

    end_time = time.time()
    print("Total time: {}".format(end_time - start_time))

if __name__ == '__main__':
    main()                  # 18 秒
'''

# 同时执行的两个并发线程
'''
from threading import Thread
import time

def my_counter():
    i = 0
    for _ in range(100000000):
        i = i + 1
    return True

def main():
    thread_array = {}
    start_time = time.time()
    for tid in range(2):
        t = Thread(target=my_counter)
        t.start()
        thread_array[tid] = t

    for i in range(2):
        thread_array[i].join()
    end_time = time.time()
    print("Total time: {}".format(end_time - start_time))

if __name__ == '__main__':
    main()                  # 27 秒

'''

'''
from threading import Thread, Lock
import os, time

def work():
    global n
    lock.acquire()
    temp = n
    time.sleep(0.1)
    n = temp - 1
    lock.release()

if __name__ == '__main__':
    lock = Lock()
    n = 100
    l = []
    for i in range(100):
        p = Thread(target=work)
        l.append(p)
        p.start()

    for p in l:
        p.join()

    print(n)    ##结果肯定为0，由原来的并发执行变成串行，牺牲了执行效率保证了数据安全，不加锁则结果可能为99
'''


#五 多线程性能测试
#如果并发的多个任务是计算密集型：多进程效率高
'''
from multiprocessing import Process
import os, time
from threading import Thread

def work():
    res = 0
    for i in range(100000000):
        res *= 1

if __name__ == '__main__':
    l = []
    print(os.cpu_count())
    start = time.time()
    for i in range(4):
        #p = Process(target=work)   #12
        p = Thread(target=work) #32

        l.append(p)
        p.start()

    for p in l:
        p.join()

    stop = time.time()
    print('run time is %s' %(stop - start))
'''

#如果并发的多个任务是I/O密集型：多线程效率高

from multiprocessing import Process
from threading import Thread
import os, time

def work():
    time.sleep(2)
    print("====>")

if __name__ == '__main__':
    l = []
    start = time.time()
    for i in range(409):
        p = Process(target=work)  #3
        #p = Thread(target=work)  #2
        l.append(p)
        p.start()

    for p in l:
        p.join()
    stop = time.time()
    print('run time is %s' % (stop - start))

