
# Event
# 列如，有多个工作线程尝试链接MySQL,我们想要在链接前确保MySQL服务正常才让那些
# 工作线程去连接MySQL服务器,如果连接不成功，都会尝试重新链接。那么我们就可以采用
# threading.Event机制来协调各个工作线程的链接操作

# event.isSet(): 返回event的状态值
# event.wait(): 如果event.isSet()==False将阻塞线程
# event.set(): 设置event的状态值为True,所有阻塞池线程激活进入就绪状态，等待操作系统调度
# event.clear(): 恢复event的状态值为False

'''
from threading import Thread, Event
import threading
import time, random

def conn_mysql():
    count = 1
    while not event.is_set():
        if count > 3:
            raise TimeoutError('connect time out!')
        print('<%s> The %s attempt connect' % (threading.current_thread().getName(), count))
        event.wait(0.5)
        count += 1
    print('<%s>connect success!' % threading.current_thread().getName())

def check_mysql():
    print('[%s] in check mysql' % threading.current_thread().getName())
    time.sleep(random.randint(2, 4))
    event.set()

if __name__ == '__main__':
    event = Event()
    conn1 = Thread(target=conn_mysql)
    conn2 = Thread(target=conn_mysql)
    check = Thread(target=check_mysql)

    conn1.start()
    conn2.start()
    check.start()

'''

'''


from threading import Thread, Event
import time

event = Event()
print(event.isSet())
# event.wait()
# event.set()

def student(name):
    print('student % in tingke' % name)
    event.wait(2)
    print('student % in kejiPlay' % name)

def teacher(name):
    print('teacher %s in shouke' % name)
    time.sleep(7)
    event.set()

if __name__ == '__main__':
    stu1 = Thread(target=student, args=('alex',))
    stu2 = Thread(target=student, args=('wxxx',))
    stu3 = Thread(target=student, args=('yxx',))
    t1 = Thread(target=teacher, args=('egon',))

    stu1.start()
    stu2.start()
    stu3.start()
    t1.start()

'''

from threading import Thread, Event, currentThread
import time

event = Event()

def conn():
    n = 0
    while not event.is_set():
        if n == 3:
            print('%s try too many times' % currentThread().getName())
            return

        print('%s try %s' % (currentThread().getName(), n))
        event.wait(0.5)
        n += 1

    print('%s is connectd' % currentThread().getName())

def check():
    print('%s is checking' % currentThread().getName())
    time.sleep(5)
    event.set()

if __name__ == '__main__':
    for i in range(3):
        t = Thread(target=conn)
        t.start()
    t = Thread(target=check)
    t.start()
