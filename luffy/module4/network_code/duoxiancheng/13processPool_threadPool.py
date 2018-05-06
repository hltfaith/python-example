# concurrent.futures：模块提供了高度封装的异步调用接口
# ThreadPoolExecutor: 线程池, 提供异步调用
# ProcessPoolExecutor: 进程池, 提供异步调用


# 基本方法
# 1、submit(fn, *args, **kwargs)
# 异步提交任务

# 2、map(func, *iterables, timeout=None, chunksize=1)
# 取代for循环submit的操作

# 3、shutdown(wait=True)
# 相当于进程池的pool.close() + pool.join()操作
# wait=True,等待池内所有任务执行完毕回收完资源后才继续
# wait=False, 立即返回，并不会等待池内的任务执行完毕
# 但不管wait参数为何值, 整个程序都会等到所有任务执行完毕
# submit 和 map必须在shutdown之前

# 4、result(timeout=None)
# 获得结果

# 5、add_done_callback(fn)
# 回调函数
'''
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import os, time, random

def task(n):
    print('%s is runing' % os.getpid())
    time.sleep(random.randint(1, 3))
    return n**2

if __name__ == '__main__':
    #executor = ProcessPoolExecutor(max_workers=3)
    executor = ThreadPoolExecutor(max_workers=3)

    futures = []
    for i in range(11):
        future = executor.submit(task, i)
        futures.append(future)

    executor.shutdown(True)
    print('+++>')
    for future in futures:
        print(future.result())
'''

from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from threading import currentThread
import os, time, random

def task():
    print('name: %s pid:%s run' %(currentThread().getName(), os.getpid()))
    time.sleep(random.randint(1, 3))

if __name__ == '__main__':
    pool = ThreadPoolExecutor(5)

    for i in range(10):
        pool.submit(task, )

    pool.shutdown(wait=True)

    print('master')
