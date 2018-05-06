
# 定时3秒
'''
from threading import Timer

def hello():

    print('hello, world')

t = Timer(3, hello)
t.start()
'''

# 验证码示例

from threading import Timer
import random

class Code:
    def __init__(self):
        self.make_cache()

    def make_cache(self, interval=5):
        self.cache = self.make_code()
        print(self.cache)
        self.t = Timer(interval, self.make_cache)
        self.t.start()

    def make_code(self, n=4):
        res = ''
        for i in range(n):
            s1 = str(random.randint(0, 9))
            s2 = chr(random.randint(65, 90))
            res += random.choice([s1, s2])
        return res

    def check(self):
        while True:
            code = input('pelase inpute your code>>: ').strip()
            if code.upper() == self.cache:
                print('verifiction code success!')
                self.t.cancel()
                break

obj = Code()
obj.check()
