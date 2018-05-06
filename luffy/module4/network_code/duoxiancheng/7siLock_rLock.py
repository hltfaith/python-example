
# 所谓死锁：是指两个或两个以上的进程或线程在执行过程中，因争夺资源而造成的一种
# 互相等待的现象，若无外力作用，他们都将无法推进下去。此时成系统处于死锁状态或
# 系统产生了死锁，这些永远在互相等待的进程称为死锁进程。
'''
from threading import Thread, Lock
import time
mutexA = Lock()
mutexB = Lock()

class MyThread(Thread):
    def run(self):
        self.func1()
        self.func2()

    def func1(self):
        mutexA.acquire()
        print('%s get A Lock' % self.name)

        mutexB.acquire()
        print('%s get B Lock' % self.name)
        mutexB.release()

        mutexA.release()

    def func2(self):
        mutexB.acquire()
        print('%s is get B Lock' % self.name)
        time.sleep(2)

        mutexA.acquire()
        print('%s is get A Lock' % self.name)
        mutexA.release()

        mutexB.release()

if __name__ == '__main__':
    for i in range(10):
        t = MyThread()
        t.start()

'''

# 递归锁
# 在python中为了支持在同一线程中多次请求同一资源，python提供了可重入锁RLock
# 这个RLock内部维护着一个Lock和一个counter变量,counter记录了acquire的次数
# 从而使得资源可以被多次require，直到一个线程所有的acquire都被release，其他
# 的线程才能获得资源。 上面的例子如果使用RLock代替Lock，则不会发生死锁，二者
# 的区别是：递归锁可以连续acquire多次，而互斥锁只能acquire一次

from threading import Thread, RLock
import time

mutexA = mutexb = RLock()  # 一个进程拿到锁，counter加1,该线程内又碰到加锁的情况，则counter继续加1,这期间所有其他线程释放所有锁，即counter递减到0为止

class MyThread(Thread):
    def run(self):
        self.func1()
        self.func2()

    def func1(self):
        mutexA.acquire()
        print('%s get A Lock' % self.name)

        mutexb.acquire()
        print('%s get B Lock' % self.name)
        mutexb.release()

        mutexA.release()

    def func2(self):
        mutexb.acquire()
        print('%s is get B Lock' % self.name)

        time.sleep(2)

        mutexA.acquire()
        print('%s is get A Lock' % self.name)
        mutexA.release()

        mutexb.release()

if __name__ == '__main__':
    for i in range(10):
        t = MyThread()
        t.start()
