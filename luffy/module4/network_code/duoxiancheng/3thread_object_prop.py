
# Thread对象的其他属性或方法

# Thread实例对象的方法
# isAlive(): 返回线程是否活动的
# getName(): 返回线程名
# setName(): 设置线程名

# threading 模块提供的一些方法
# threading.currentThread(): 返回当前的线程变量
# threading.enumerate(): 返回一个包含正在运行的线程的list. 正在运行指线程启动后、结束前，不包括启动前和终止后的线程.
# threading.activeCount(): 返回正在运行的线程数量,与len(threading.enumerate())有相同的结果。

'''
from threading import Thread
import threading
from multiprocessing import Process
import os

def work():
    import time
    time.sleep(3)
    print(threading.current_thread().getName())

if __name__ == '__main__':
    # 在主进程下开启线程
    t = Thread(target=work)
    t.start()

    print(threading.current_thread().getName())
    print(threading.current_thread())  #主线程
    print(threading.enumerate())     #连同主进程在内的两个运行的进程
    print(threading.active_count())

    print('主进程')

'''


# 主线程等待子线程结束
'''
from threading import Thread
import time

def sayhi(name):
    time.sleep(2)
    print('%s say hello' % name)

if __name__ == '__main__':
    t = Thread(target=sayhi, args=('egon', ))
    t.start()
    t.join()

    print('主线程')
    print(t.is_alive())
'''

from threading import Thread, currentThread, active_count, enumerate
import time

def task():
    print('%s is running' % currentThread().getName())
    time.sleep(2)
    print('%s is done' % currentThread().getName())

if __name__ == '__main__':
    t = Thread(target=task, name='子线程')
    t.start()

    t.setName('儿子进程1')
    t.join()
    print(t.getName())
    currentThread().setName('主线程')
    print(t.isAlive())

    print('主线程', currentThread().getName())

    t.join()
    print(active_count())

    print(enumerate())
