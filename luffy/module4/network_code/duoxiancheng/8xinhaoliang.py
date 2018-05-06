
# 信号量
# 信号量也是一把锁，可以指定信号量为5,对比互斥锁同一时间只能有一个任务抢到锁去
# 执行，信号量同一时间可以有5个任务拿到锁去执行，如果说互斥锁是合租房屋的人去抢
# 一个厕所，那么信号量就相当于一群路人争抢公共厕所，公共厕所有多少坑位，这意味着
# 同一时间可以有多少个人上公共厕所，但公共厕所容纳的人数是一定的，这便是信号量的大小

from threading import Thread, Semaphore
import threading
import time

def func():
    sm.acquire()
    print('%s get sm ' % threading.current_thread().getName())
    time.sleep(3)
    sm.release()

if __name__ == '__main__':
    sm = Semaphore(5)
    for i in range(23):
        t = Thread(target=func)
        t.start()
        
