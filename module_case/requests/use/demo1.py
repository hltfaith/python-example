
'''

什么是Requests
Requests是用python语言基于urllib编写的，采用的是Apache2 Licensed开源协议的HTTP库
如果你看过上篇文章关于urllib库的使用，你会发现，其实urllib还是非常不方便的，而Requests它会比urllib更加方便，
可以节约我们大量的工作。（用了requests之后，你基本都不愿意用urllib了）一句话，requests是python实现的最简单易用的HTTP库，
建议爬虫使用requests库。

默认安装好python之后，是没有安装requests模块的，需要单独通过pip安装


'''

'''
# 总体功能的一个演示
import requests

response = requests.get("http://www.baidu.com")
print(type(response))
print(response.status_code)
print(type(response.text))
print(response.text)
print(response.cookies)
print(response.content)
print(response.content.decode("utf-8"))
'''

'''
# 避免乱码的问题发生
import requests
response =requests.get("http://www.baidu.com")
response.encoding="utf-8"
print(response.text)
'''

'''
# requests里提供个各种请求方式
import requests
requests.post("http://httpbin.org/post")
requests.put("http://httpbin.org/put")
requests.delete("http://httpbin.org/delete")
requests.head("http://httpbin.org/get")
requests.options("http://httpbin.org/get")

'''

'''
# Requests模块允许使用params关键字传递参数，以一个字典来传递这些参数
import requests
data = {
    "name":"zhaofan",
    "age":22
}
response = requests.get("http://httpbin.org/get",params=data)
print(response.url)
print(response.text)
'''

'''
# 解析json
import requests
import json

response = requests.get("http://httpbin.org/get")
print(type(response.text))
print(response.json())
print(json.loads(response.text))
print(type(response.json()))
'''


'''
# 添加headers
import requests
headers = {

    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}
response = requests.get("http://httpbin.org/get", headers=headers)

print(response.text)
'''


'''
# 基本POST请求
import requests

data = {
    "name":"zhaofan",
    "age":23
}
response = requests.post("http://httpbin.org/post", data=data)
print(response.text)
'''


'''
# 响应
import requests

response = requests.get("http://www.baidu.com")
print(type(response.status_code),response.status_code)
print(type(response.headers),response.headers)
print(type(response.cookies),response.cookies)
print(type(response.url),response.url)
print(type(response.history),response.history)

'''


'''
# 状态码判断

import requests

response= requests.get("http://www.baidu.com")
if response.status_code == requests.codes.ok:
    print("访问成功")
'''


'''
# 文件上传
import requests
files= {"files":open("git.jpeg","rb")}
response = requests.post("http://httpbin.org/post",files=files)
print(response.text)
'''


'''
# 获取cookie
import requests

response = requests.get("http://www.baidu.com")
print(response.cookies)

for key,value in response.cookies.items():
    print(key+"="+value)

'''


'''
# 会话维持
import requests
s = requests.Session()
s.get("http://httpbin.org/cookies/set/number/123456")
response = s.get("http://httpbin.org/cookies")
print(response.text)
'''

'''
# 证书验证
import requests
from requests.packages import urllib3
urllib3.disable_warnings()
response = requests.get("https://www.zhihu.com",verify=False)
print(response.status_code)
'''

'''
# 代理设置
import requests

proxies= {
    "http":"http://127.0.0.1:9999",
    "https":"http://127.0.0.1:8888"
}
response = requests.get("https://www.baidu.com", proxies=proxies)
print(response.text)
'''

'''
# 认证设置
import requests

from requests.auth import HTTPBasicAuth

response = requests.get("http://120.27.34.24:9001/",auth=HTTPBasicAuth("user","123"))
print(response.status_code)
'''

# 异常
import requests

from requests.exceptions import ReadTimeout,ConnectionError,RequestException


try:
    response = requests.get("http://httpbin.org/get",timeout=0.1)
    print(response.status_code)
except ReadTimeout:
    print("timeout")
except ConnectionError:
    print("connection Error")
except RequestException:
    print("error")

