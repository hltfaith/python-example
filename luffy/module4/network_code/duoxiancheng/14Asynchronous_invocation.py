
'''
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from multiprocessing import Pool
import json
import os
import requests

def get_page(url):
    print('<进程%s> get %s' %(os.getpid(), url))
    respone=requests.get(url)
    if respone.status_code == 200:
        return {'url':url, 'text': respone.text}

def parse_page(res):
    res = res.result()
    print('<进程%s> parse %s' % (os.getpid(), res['url']))
    parse_res = 'url:<%s> size:[%s]\n' % (res['url'], len(res['text']))
    with open('db.txt', 'a') as f:
        f.write(parse_res)

if __name__ == '__main__':
    urls = [
        'https://www.baidu.com',
        'https://www.python.org',
        'https://www.openstack.org',
        'https://help.github.com',
        'http://www.sina.com.cn'
    ]
    p = ProcessPoolExecutor(3)
    for url in urls:
        p.submit(get_page, url).add_done_callback(parse_page)
'''

# 提交任务的两种方式
# 1. 同步调用：提交完任务后，就在原地等待任务执行完毕，拿到结果，在执行下一行代码，导致程序是串行执行
'''
from concurrent.futures import ThreadPoolExecutor
import time
import random

def la(name):
    print('%s is laing' % name)
    time.sleep(random.randint(3, 5))
    res = random.randint(7, 13)*'#'
    return {'name':name, 'res':res}

def weigh(shit):
    name = shit['name']
    size = len(shit['res'])
    print('%s 拉了 <%s> kg' % (name, size))

if __name__ == '__main__':
    pool = ThreadPoolExecutor(13)
    shit1 = pool.submit(la, 'alex').result()
    weigh(shit1)

    shit2 = pool.submit(la, 'wupeiqi').result()
    weigh(shit2)

    shit3 = pool.submit(la, 'yuanhao').result()
    weigh(shit3)
'''

# 2. 异步调用:提交完任务后，不地等待任务执行完毕

from concurrent.futures import ThreadPoolExecutor
import time
import random

def la(name):
    print('%s is laing' % name)
    time.sleep(random.randint(3, 5))
    res = random.randint(7, 13)*'#'
    return {'name':name, 'res':res}

def weigh(shit):
    shit = shit.result()
    name = shit['name']
    size = len(shit['res'])
    print('%s 拉了 <%s>kg' %(name, size))

if __name__ == '__main__':
    pool = ThreadPoolExecutor(13)
    pool.submit(la, 'alex').add_done_callback(weigh)
    pool.submit(la, 'wupeiqi').add_done_callback(weigh)
    pool.submit(la, 'yuanhao').add_done_callback(weigh)
