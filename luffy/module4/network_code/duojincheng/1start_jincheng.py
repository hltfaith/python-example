
# 方式一
'''
from multiprocessing import Process
import time

def task(name):
    print('%s is running' % name)
    time.sleep(3)
    print('%s is running' % name)

if __name__ == '__main__':
    p = Process(target=task, args=('子进程', ))
    p.start()

    print('master')

'''

# 方式二
from multiprocessing import Process
import time

class myprocess(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print('%s is running' % self.name)
        time.sleep(3)
        print('%s is running' % self.name)

if __name__ == '__main__':
    p = myprocess('子进程')
    p.start()
    print('master')











