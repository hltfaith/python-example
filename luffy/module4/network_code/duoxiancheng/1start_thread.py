
#方式一
'''
from threading import Thread
import time

def sayhi(name):
    time.sleep(2)
    print('%s say hello' % name)

if __name__ == '__main__':
    t = Thread(target=sayhi, args=('egon',))
    t.start()
    print('主线程')
'''

#方式二
from threading import Thread
import time


class Sayhi(Thread):
    def __init__(self,name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(2)
        print('%s say hello' % self.name)

if __name__ == '__main__':
    t = Sayhi('egon')
    t.start()
    print('主线程')

