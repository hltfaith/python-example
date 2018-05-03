
# 守护进程
'''
from multiprocessing import Process
import time
import random

def task(name):
    print('%s is runnning.' % name)
    time.sleep(random.randrange(1, 3))
    print('%s is done.' % name)

if __name__ == '__main__':
    p = Process(target=task, args=('egon', ))
    p.daemon = True   # 一定要在p.start()前设置, 设置p为守护子进程, 并且父进程代码执行结束, p即终止运行
    p.start()

    print('master')
'''


#练习题

from multiprocessing import Process
import time
def foo():
    print('123')
    time.sleep(5)
    print('123end')

def bar():
    print('456')
    time.sleep(3)
    print('456end')

if __name__ == '__main__':
    p1 = Process(target=foo)
    p2 = Process(target=bar)

    p1.daemon = True
    p1.start()
    p2.start()

    print('master')

