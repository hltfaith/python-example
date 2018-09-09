#join方法
# from multiprocessing import Process
# import time,os
#
# def task():
#     print('%s is running,parent id is <%s>' %(os.getpid(),os.getppid()))
#     time.sleep(3)
#     print('%s is done,parent id is <%s>' %(os.getpid(),os.getppid()))
#
# if __name__ == '__main__':
#     p=Process(target=task,)
#     p.start()
#
#     p.join()
#     print('主',os.getpid(),os.getppid())
#     print(p.pid)


# from multiprocessing import Process
# import time,os
#
# def task(name,n):
#     print('%s is running' %name)
#     time.sleep(n)
#
#
# if __name__ == '__main__':
#     start=time.time()
#     p1=Process(target=task,args=('子进程1',5))
#     p2=Process(target=task,args=('子进程2',3))
#     p3=Process(target=task,args=('子进程3',2))
#     p_l=[p1,p2,p3]
#
#     # p1.start()
#     # p2.start()
#     # p3.start()
#     for p in p_l:
#         p.start()
#
#     # p1.join()
#     # p2.join()
#     # p3.join()
#     for p in p_l:
#         p.join()
#
#     print('主',(time.time()-start))





# from multiprocessing import Process
# import time,os
#
# def task(name,n):
#     print('%s is running' %name)
#     time.sleep(n)
#
#
# if __name__ == '__main__':
#     start=time.time()
#     p1=Process(target=task,args=('子进程1',5))
#     p2=Process(target=task,args=('子进程2',3))
#     p3=Process(target=task,args=('子进程3',2))
#
#     p1.start()
#     p1.join()
#     p2.start()
#     p2.join()
#     p3.start()
#     p3.join()
#
#     print('主',(time.time()-start))


#了解:is_alive
from multiprocessing import Process
import time,os

def task():
    print('%s is running,parent id is <%s>' %(os.getpid(),os.getppid()))
    time.sleep(3)
    print('%s is done,parent id is <%s>' %(os.getpid(),os.getppid()))

if __name__ == '__main__':
    # p=Process(target=task,)
    # p.start()
    # # print(p.is_alive())
    # p.join()
    # print('主',os.getpid(),os.getppid())
    # print(p.pid)
    # # print(p.is_alive())



    p=Process(target=task,name='sub——Precsss')
    p.start()
    p.terminate()
    time.sleep(3)
    print(p.is_alive())
    print('主')
    print(p.name)
















