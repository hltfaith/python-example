from multiprocessing import Process,Queue
import time

def producer(q):
    for i in range(10):
        res='包子%s' %i
        time.sleep(0.5)
        print('生产者生产了%s' %res)

        q.put(res)

def consumer(q):
    while True:
        res=q.get()
        if res is None:break
        time.sleep(1)
        print('消费者吃了%s' % res)



if __name__ == '__main__':
    #容器
    q=Queue()

    #生产者们
    p1=Process(target=producer,args=(q,))
    p2=Process(target=producer,args=(q,))
    p3=Process(target=producer,args=(q,))

    #消费者们
    c1=Process(target=consumer,args=(q,))
    c2=Process(target=consumer,args=(q,))

    p1.start()
    p2.start()
    p3.start()
    c1.start()
    c2.start()

    p1.join()
    p2.join()
    p3.join()
    q.put(None)
    q.put(None)
    print('主')

