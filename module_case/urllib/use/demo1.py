
# urllib 第一个爬虫程序
# import urllib.request
# respone = urllib.request.urlopen('http://www.baidu.com')
# print(respone.read().decode('utf-8'))

'''

# POST 请求包

import urllib.parse
import urllib.request

data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
print(data)
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read())


'''

'''
# timeout参数的使用

import socket
import urllib.request

try:

    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
    print(response.read())

except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')


'''

'''
import urllib.request

response = urllib.request.urlopen('https://www.python.org')
print(type(response))
# print(response.read())
# print(response.getheaders())
print(response.status)

'''


'''
# 设置Headers

from urllib import request, parse


url = 'http://httpbin.org/post'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Host': 'httpbin.org'
}

dict = {
    'name': 'changhao'
}

data = bytes(parse.urlencode(dict), encoding='utf8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))


'''

'''
# 代理,ProxyHandler

import urllib.request

proxy_handler = urllib.request.ProxyHandler({
    'http': 'http://119.57.109.129:53281',
    # 'https': 'https://123.117.36.200:9000'
})
opener = urllib.request.build_opener(proxy_handler)
response = opener.open('http://httpbin.org/get')
print(response.read())

'''


'''
# cookie,HTTPCookiProcessor
# cookie中保存中我们常见的登录信息，有时候爬取网站需要携带cookie信息访问,
# 这里用到了http.cookijar，用于获取cookie以及存储cookie

import http.cookiejar, urllib.request
cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name+"="+item.value)

'''


'''

# URLError,HTTPError，HTTPError是URLError的子类

from urllib import request,error
try:
    response = request.urlopen("http://pythonsite.com/1111.html")
except error.HTTPError as e:
    print(e.reason)
    print(e.code)
    print(e.headers)
except error.URLError as e:
    print(e.reason)

else:
    print("reqeust successfully")


'''




'''

# 
import socket

from urllib import error,request

try:
    response = request.urlopen("http://www.pythonsite.com/",timeout=0.001)
except error.URLError as e:
    print(type(e.reason))
    if isinstance(e.reason,socket.timeout):
        print("time out")

'''

'''
# URL解析
from urllib.parse import urlparse

result = urlparse("http://www.baidu.com/index.html;user?id=5#comment")
print(result)
'''

'''
# urlunpars 用于拼接
from urllib.parse import urlunparse

data = ['http','www.baidu.com','index.html','user','a=123','commit']
print(urlunparse(data))
'''

# urlencode
# 这个方法可以将字典转换为url参数，例子如下
from urllib.parse import urlencode

'''
params = {
    "name":"zhaofan",
    "age":23,
}
base_url = "http://www.baidu.com?"

url = base_url+urlencode(params)
print(url)

'''



