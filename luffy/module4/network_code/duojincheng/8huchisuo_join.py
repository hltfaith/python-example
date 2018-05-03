from multiprocessing import Process,Lock
import time,json

def search(name):
    dic=json.load(open('db.txt'))
    print('\033[43m%s 查到剩余票数%s\033[0m' %(name,dic['count']))

def get(name):
    dic=json.load(open('db.txt'))
    time.sleep(1) #模拟读数据的网络延迟
    if dic['count'] >0:
        dic['count']-=1
        time.sleep(1) #模拟写数据的网络延迟
        json.dump(dic,open('db.txt','w'))
        print('\033[46m%s 购票成功\033[0m' %name)

def task(name,):
    search(name)
    get(name)

if __name__ == '__main__':
    for i in range(10):
        name='<路人%s>' %i
        p=Process(target=task,args=(name,))
        p.start()
        p.join()
