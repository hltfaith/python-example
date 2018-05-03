
# 互斥锁 运行结果错乱
'''
from multiprocessing import Process
import os, time

def work():
    print('%s is running...' % os.getpid())
    time.sleep(3)
    print('%s is done....' % os.getpid())

if __name__ == '__main__':
    for i in range(3):
        p = Process(target=work)
        p.start()
'''

# 由并发变成了串行, 牺牲了运行效率, 但避免了竞争
from multiprocessing import Process, Lock
import os,time
def work(lock):
    lock.acquire()   # 加锁
    print('%s is running' % os.getpid())
    time.sleep(2)
    print('%s is done..' % os.getpid())
    lock.release()  # 释放锁

if __name__ == '__main__':
    lock = Lock()
    for i in range(3):
        p = Process(target=work, args=(lock, ))
        p.start()
