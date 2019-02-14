
'''

requests 模块高级：
    - cookie:
        基于用户的用户数据
        - 需求： 爬取张三用户的豆瓣网的个人主页
    - cookie作用： 服务器端使用cookie来记录客户端的状态
    - 代理：



import requests

session = requests.session()

login_url = 'https://accounts.douban.com/login'

data = {
    'source': 'None',
    'redir': 'https://www.douban.com/people/185687620/',
    'form_email': '15027900535',
    'form_password': 'bobo@15027900535',
    'login': '登录',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
}

login_response = session.post(url=login_url, headers=headers, data=data)

# 对个人主页发起请求(session (cookie)), 获取响应页面数据
url = 'https://www.douban.com/people/185687620'
response = session.get(url=url, headers=headers,)
page_text = response.text

with open('./douban110.html', 'w', encoding='utf-8') as fp:
    fp.write(page_text)

'''


'''
代理操作
    -1. 代理： 第三方代理本体执行相关的事物，生活:代购
    -2. 为什么使用代理
        - 反爬操作
        - 反反爬手段
    -3. 分类：
        - 正向代理： 代替客户端获取数据
        - 反向代理： 代替服务器提供数据
    -4. 免费代理IP的网站提供商
        - www.goubanjia.com
        - 快代理
        - 西祠代理
    -5. 代码：


import requests

url = 'https://www.baidu.com/s?ie=utf-8&wd=ip'

# 代理IP
proxy = {
    'http': '118.174.232.38:56797'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
}

# 更换网络IP
response = requests.get(url=url, proxies=proxy, headers=headers)

with open('./daili.html', 'w', encoding='utf-8') as fb:
    fb.write(response.text)

'''


'''

验证码处理- 打码平台
验证码处理：
    - 1.手动识别验证码
    - 2.云打码平台自动识别验证码
    
云打码平台处理验证码的实现流程:
    - 1. 对携带验证码的页面数据进行抓取


'''

import requests
from lxml import etree

