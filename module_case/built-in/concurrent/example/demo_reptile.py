
'''

简单的循环串行
这一种方法相对来说是最慢的，因为一个一个循环，耗时是最长的，是所有的时间总和



import requests

url_list = [

    'http://www.baidu.com',
    'http://www.pythonsite.com',
    'http://www.cnblogs.com/'

]

for url in url_list:
    result = requests.get(url)
    print(result.text)


'''


'''

通过线程池
通过线程池的方式访问，这样整体的耗时是所有连接里耗时最久的那个，相对循环来说快了很多


import requests
from concurrent.futures import ThreadPoolExecutor

def fetch_request(url):
    result = requests.get(url)
    print(result.text)

url_list = [

    'http://www.baidu.com',
    'http://www.bing.com',
    'http://www.cnblogs.com/'

]

pool = ThreadPoolExecutor(10)

for url in url_list:
    pool.submit(fetch_request, url)

pool.shutdown(True)


'''


'''
Python之回调函数
在计算机程序设计中，回调函数，或简称回调（Callback），
是指通过函数参数传递到其它代码的，某一块可执行代码的引用。这一设计允许了底层代码调用在高层定义的子程序。


def my_callback(input):
    print('function my_callback was called with %s input' % (input, ))

def caller(input, func):
    func(input)

for i in range(5):
    caller(i, my_callback)

'''


'''

线程池+回调函数
这里定义了一个回调函数callback


from concurrent.futures import ThreadPoolExecutor
import requests

def fetch_async(url):
    response = requests.get(url)
    return response

def callback(future):
    print(future.result().text)

url_list = [
    'http://www.baidu.com',
    'http://www.bing.com',
    'http://www.cnblogs.com/'
]

pool = ThreadPoolExecutor(5)

for url in url_list:
    v = pool.submit(fetch_async, url)
    v.add_done_callback(callable)

pool.shutdown()

'''


'''

通过进程池
通过进程池的方式访问，同样的也是取决于耗时最长的，但是相对于线程来说，
进程需要耗费更多的资源，同时这里是访问url时IO操作，所以这里线程池比进程池更好



import requests
from concurrent.futures import ProcessPoolExecutor

def fetch_request(url):
    result = requests.get(url)
    print(result.text)

url_list = [
    'http://www.baidu.com',
    'http://www.bing.com',
    'http://www.cnblogs.com/'
]

pool = ProcessPoolExecutor(10)

for url in url_list:
    # 去进程池中获取一个线程，子进程程去执行fetch_request方法
    pool.submit(fetch_request, url)

pool.shutdown(True)

'''


'''

进程池+回调函数
这种方式和线程+回调函数的效果是一样的，相对来说开进程比开线程浪费资源

'''

from concurrent.futures import ProcessPoolExecutor
import requests


def fetch_async(url):
    reponse = requests.get(url)
    return reponse

def callback(future):
    print(future.result().text)

url_list = [

    'http://www.baidu.com',
    'http://www.bing.com',
    'http://www.cnblogs.com/'

]

pool = ProcessPoolExecutor(5)

for url in url_list:
    v = pool.submit(fetch_async, url)
    v.add_done_callback(callable)

pool.shutdown()





