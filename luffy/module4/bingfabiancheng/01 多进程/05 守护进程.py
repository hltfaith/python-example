# from multiprocessing import Process
# import time
#
# def task(name):
#     print('%s is running' %name)
#     time.sleep(2)
#     p=Process(target=time.sleep,args=(3,))
#     p.start()
#
#
# if __name__ == '__main__':
#     p=Process(target=task,args=('子进程1',))
#     p.daemon=True
#     p.start()
#
#     p.join()
#     print('主')


#练习题
from multiprocessing import Process

import time
def foo():
    print(123)
    time.sleep(1)
    print("end123")

def bar():
    print(456)
    time.sleep(3)
    print("end456")

if __name__ == '__main__':
    p1=Process(target=foo)
    p2=Process(target=bar)

    p1.daemon=True
    p1.start()
    p2.start()
    print("main-------")








