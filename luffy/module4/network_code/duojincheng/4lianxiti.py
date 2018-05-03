
# 进程之间内存空间隔离

from multiprocessing import Process

n = 100

def work():
    global n
    n = 0
    print('子进程内: ', n)


if __name__ == '__main__':
    p = Process(target=work)
    p.start()
    p.join()

    print('主进程内: ', n)
