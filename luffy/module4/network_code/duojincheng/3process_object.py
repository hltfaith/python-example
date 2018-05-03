
# join() 使用
'''
from multiprocessing import Process
import time, os
import random

def task():
    print('%s is piaoing' % os.getpid())
    time.sleep(3)
    print('%s is piao end' % os.getpid())

if __name__ == '__main__':
    p = Process(target=task)
    p.start()
    p.join()

    print('master')
'''

# join() 指定进程等待
'''
from multiprocessing import Process
import time
import random
import os

def task(name):
    print('%s is running' % name)
    time.sleep(random.randint(1, 3))
    print('%s is done' % name)

if __name__ == '__main__':
    p1 = Process(target=task, args=('egon', ))
    p2 = Process(target=task, args=('alex', ))
    p3 = Process(target=task, args=('changhao', ))

    p1.start()
    p2.start()
    p3.start()

    p1.join()

    print('master')
'''


# terminate 和 is_alive
'''
from multiprocessing import Process
import time
import random

def task(name):
    print('%s is piaoing' %name)
    time.sleep(random.randrange(1,5))
    print('%s is piao end' %name)

if __name__ == '__main__':
    p1=Process(target=task,args=('egon',))
    p1.start()

    p1.terminate()#关闭进程,不会立即关闭,所以is_alive立刻查看的结果可能还是存活
    print(p1.is_alive()) #结果为True

    print('主')
    print(p1.is_alive()) #结果为False
'''

# 进程对象的其他属性： name 和 pid
'''
from multiprocessing import Process
import time
import random

def task(name):
    print('%s is piaoing' % name)
    time.sleep(random.randint(1, 5))
    print('%s is piao end' % name)

if __name__ == '__main__':
    p1 = Process(target=task, args=('engon', ), name='子进程')
    p1.start()
    print(p1.name, p1.pid)
'''

# 练习题
from multiprocessing import Process
import time
import random

def task(n):
    time.sleep(1)
    print('------------> %s' % n)

if __name__ == '__main__':
    start = time.time()
    p1 = Process(target=task, args=(1, ))
    p2 = Process(target=task, args=(2,))
    p3 = Process(target=task, args=(3,))

    p1.start()
    p1.join()
    p2.start()
    p2.join()
    p3.start()
    p3.join()

    # p1.join()
    # p2.join()
    # p3.join()

    print('------------> 4')

