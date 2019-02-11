
'''
request 简介
- 1.什么是requests模块
    - python原生一个基于网络请求的模块，模拟浏览器发起请求。
- 2.为什么要使用requests模块
    - 1.手动处理url编码
    - 2.手动处理post请求的参数 urlencode() .decode()
    - 3.cookie的代理的操作比较繁琐
        - 创建一个cookiejar对象
        - 创建一个handler对象
        - 创建一个operner

        - 创建handler对象, 代理ip和端口封装到该对象

- 3.requests如何被使用
    安装: pip install requests
    使用流程：
        1.指定url
        2.使用requests模块发起请求
        3.获取响应数据
        4.进行持久化存储
- 4.通过5个基于requests模块的爬虫项目对该模块进行系统学习和巩固
    - get 请求
    - post 请求
    - ajax的get请求
    - ajax的post请求
    - 综合
'''


'''
requsts-get请求

- 需求: 爬取搜狗首页的页面数据


import requests

# 指定url
url = 'https://www.sogou.com/'

# 发起get请求： get方法会返回请求成功的相应对象
response = requests.get(url=url)

# 获取响应中的数据值: text可以获取响应对象中字符串形式的页面数据
page_data = response.text
print(page_data)

# 持久化操作
with open('./sogou.html', 'w', encoding='utf-8') as fp:
    fp.write(page_data)

'''

'''
requests (response 常用属性)

response 对象中其他重要的属性

import requests

url = 'https://www.sogou.com'

response = requests.get(url=url)

# content获取的是response对象中二进制(byte)类型的页面数据
print(response.content)

# 返回一个响应状态码
print(response.status_code)

# 返回响应头信息
print(response.headers)

# 获取请求的url
print(response.url)

'''

'''
requests模块带参get请求方法1

-需求： 指定一个词条，获取搜狗搜索结果对应的页面数据

import requests

url = 'https://www.sogou.com/web?query=周杰伦&ie=utf-8'

response = requests.get(url=url)

page_text = response.text

with open('./zhou.html', 'w', encoding='utf-8') as fp:
    fp.write(page_text)
    
'''


'''
requests模块带参get请求方法2

方式二

import requests

url = 'https://www.sogou.com/web'

# 将参数封装到字典中
params = {
    'query': '周杰伦',
    'ie': 'utf-8'
}

response = requests.get(url=url, params=params)

print(response.status_code)
print(response.content)

'''


'''
requests模块get请求自定义请求头信息

import requests

url = 'https://www.sogou.com/web'

# 将参数封装到字典中
params = {
    'query': '周杰伦',
    'ie': 'utf-8'
}

# 自定义请求头信息
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
}

response = requests.get(url=url, params=params, headers=headers)
print(response.status_code)

'''


'''
request模块的post请求


'''
