
'''
# 需求： 爬去指定词条所在页面内容
import urllib.request
import urllib.parse

# 指定URL
url = 'https://www.sogou.com/web?query='
# url特性：url不可以存在非ASCII码的字符数据
word = urllib.parse.quote('周杰伦')
url += word

# 发请求
response = urllib.request.urlopen(url=url)

# 获取页面数据
page_text = response.read()
'''


'''
- 反爬机制：网站检查请求的UA
- User-Agent(UA): 请求载体的身份标识
- 反反爬机制：伪装爬虫程序请求的UA

import urllib.request

url = 'https://www.baidu.com'

# UA伪装
# 1. 子指定一个请求对象
headers = {
    # 存储任意的请求头信息
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
}
# 该请求对像的UA进行了成功的伪装
request = urllib.request.Request(url=url, headers=headers)

#2.针对自制定的请求对象发起请求
response = urllib.request.urlopen(request)

print(response.read())
'''

'''
post请求

import urllib.request
import urllib.parse

# 1.指定URL
url = 'https://fanyi.baidu.com/sug'

# post 请求携带的参数进行处理 流程：
# 1.将post请求参数封装到字典
data = {
    'kw': '西瓜'
}
# 2.使用parse模块中的urlencode(返回值类型为str)进行编码处理
data = urllib.parse.urlencode(data)

# 3.将步骤2的编码结果转换成byte类型
data = data.encode()

# 4.发起post请求: urlopen函数的data参数表示的就是经过处理之后的post请求携带的 参数
response = urllib.request.urlopen(url=url, data=data)

print(response.read())


'''


'''
urllib的高级操作简介



'''

