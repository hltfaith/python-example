
'''
ll = lambda x, y : x + y

print(ll(1, 3))

counters = [1, 2, 3, 4]

def inc(x):
    return x + 10

print(list(map(inc, counters)))


import functools

'''

'''
基于requests模块发起的post请求
- 需求：登陆


'''

'''
import requests

# print(requests.get('http://httpbin.org/get'))
# print(requests.post('http://httpbin.org/post'))
# print(requests.put('http://httpbin.org/put'))
#
# print(requests.delete('http://httpbin.org/delete'))
# print(requests.head('http://httpbin.org/get'))
# print(requests.options('http://httpbin.org/get'))


response = requests.get('https://s.taobao.com/search',
                        params={"q": "美女"},

                        )

with open('res.html', 'wb') as f:
    print(response.text)
    f.write(response.content)

'''

'''
import requests

res=requests.post('https://www.lagou.com/jobs/positionAjax.json',
             headers={
                    'Referer': "https://www.lagou.com/jobs/list_python",
             },
             data={
                 'first': True,
                 'pn': 2,
                 'kd': 'java高级开发'
             },
             params={
                 'gj': '3年及以下',
                 'px': 'default',
                 'yx': '25k-50k',
                 'city': '北京',
                 'needAddtionalResult': False,
                 'isSchoolJob': 0
             }
             )

comapines_list=res.json()

print(comapines_list)

'''

'''
import uuid
import requests

url = 'http://httpbin.org/cookies'
cookies = dict(sbid=str(uuid.uuid4()))

res = requests.get(url, cookies=cookies)
print(res.json())
print(res.content)

'''


'''
# 尝试获取某个网页。本例子中，我们来获取 Github 的公共时间线：
import requests

# r = requests.get('https://api.github.com/events')
r1 = requests.post('http://httpbin.org/post', data={'key': 'value'})
print(r1.text)
'''


'''
# 传递 URL 参数
import requests

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('http://httpbin.org/get', params=payload)
print(r.url)

# 注意字典里值为 None 的键都不会被添加到 URL 的查询字符串里。
'''

'''
import requests

r = requests.get('https://api.github.com/events', stream=True)
print(r.raw)
with open('a.txt', 'wb') as fd:
    for chunk in r.iter_content(10):
        fd.write(chunk)

'''


'''

import requests

r = requests.get('https://api.github.com/events')
print(r.headers)

'''




'''

Cookie¶

如果某个响应中包含一些 cookie，你可以快速访问它们

import requests

# url = 'http://httpbin.org/cookies'
# cookies = dict(cookies_are='working')
# r = requests.get(url, cookies=cookies)
# print(r.text)


s = requests.Session()

s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get("http://httpbin.org/cookies")

print(r.text)

'''

import requests

# s = requests.session()
# res1 = s.get('https://www.zhihu.com/explore')
# print(res1.cookies.get_dict())
# res2 = s.get('https://www.zhihu.com/question/30565354/answer/463324517', cookies={'abs': '123'})

# response = requests.post(url='http://httpbin.org/post', params={'a': '10'}, data={'name': 'yuan'})
#
# print(response.text)

# 发送json数据

# res1 = requests.get(url='https://www.autohome.com.cn/beijing/')  # 没有指定请求头,#默认的请求头:application/x-www-form-urlencoed
#
# res2 = requests.post(url='http://httpbin.org/post', json={'age': '22'})  # 默认的请求头:application/json)
# print(res2.json())
#
# print(res2.text)
#
# print(res1.encoding)

res = requests.get("http://bj.lianjia.com/ershoufang/")
print(res.history[0].url)
print(res.url)
















