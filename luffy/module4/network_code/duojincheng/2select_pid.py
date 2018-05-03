from multiprocessing import Process
import time, os

def task():
    print('%s is running, parent id is <%s>' % (os.getpid(), os.getppid()))
    time.sleep(3)
    print('%s is done, parent id is <%s> ' % (os.getpid(), os.getppid()))

if __name__ == '__main__':
    p = Process(target=task, )
    p.start()

    print('master: ', os.getpid(),'  ', os.getppid())

