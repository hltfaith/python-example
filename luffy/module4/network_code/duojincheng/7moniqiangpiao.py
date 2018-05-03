
# 多个进程共享同一个文件, 我们可以把文件当作是一个数据库, 用多个进程模拟多个人执行抢票任务

# 并发运行,效率高,但竞争写同一文件,数据写入错乱,只有一张票,卖成功给了10个人
'''
from multiprocessing import Process
import time, json

def search(name):
    dic = json.load(open('db.txt'))
    time.sleep(1)
    print('%s查到剩余票数%s' %(name, dic['count']))

def get(name):
    dic = json.load(open('db.txt'))
    time.sleep(1)  # 模拟读取数据延迟
    if dic['count'] > 0:
        dic['count'] -= 1
        time.sleep(1)
        json.dump(dic, open('db.txt', 'w'))
        print('%s 购票成功' % name)

def task(name):
    search(name)
    get(name)

if __name__ == '__main__':
    for i in range(10):
        name = '<路人%s>' % i
        p = Process(target=task, args=(name, ))
        p.start()
'''


# 加锁处理：购票行为由并发变成了串行,牺牲了运行效率,但保证了数据安全

from multiprocessing import Process,Lock
import json
import time

def search(name):
    time.sleep(1)
    dic=json.load(open('db.txt','r',encoding='utf-8'))
    print('<%s> 查看到剩余票数【%s】' %(name,dic['count']))


def get(name):
    time.sleep(1)
    dic=json.load(open('db.txt','r',encoding='utf-8'))
    if dic['count'] > 0:
        dic['count']-=1
        time.sleep(3)
        json.dump(dic,open('db.txt','w',encoding='utf-8'))
        print('<%s> 购票成功' %name)


def task(name,mutex):
    search(name)
    mutex.acquire()
    get(name)
    mutex.release()

if __name__ == '__main__':
    mutex=Lock()
    for i in range(10):
        p=Process(target=task,args=('路人%s' %i,mutex))
        p.start()
