# coding:utf-8
import urllib.request
import urllib.error
import urllib.parse

# headers信息，从fiddler上或浏览器上可复制下来
headers = {'Accept': 'text/html,application/xhtml+xml,
        application/xml;q=0.9,image/webp,image/apng,
        */*;q=0.8',
       'Accept-Language': 'zh-CN,zh;q=0.9',
       'User-Agent': 'Mozilla/5.0 (Windows NT 6.3;
                      Win64;
                      x64) AppleWebKit/537.36 (KHTML, 
                      like Gecko)Chrome/48.0.2564.48 
                      Safari/537.36'
       }
# POST请求的信息
value = {'source': 'index_nav',
     'form_password': 'your password',
     'form_email': 'your username'
     }
# 代理IP信息为字典格式，key为'http'，value为'代理ip：端口号'
proxy = {'http': '115.193.101.21:61234'}
try:
data = urllib.parse.urlencode(value).encode('utf8')
response = urllib.request.Request(
'https://www.douban.com/', data=data, headers=headers)
# 使用ProxyHandler方法生成处理器对象
proxy_handler = urllib.request.ProxyHandler(proxy)
# 创建代理IP的opener实例
opener = urllib.request.build_opener(proxy_handler)
# 将设置好的post信息和headers的response作为参数
html = opener.open(response)
result = html.read().decode('utf8')
print(result)
except urllib.error.URLError as e:
if hasattr(e, 'reason'):
    print('错误原因是' + str(e.reason))
except urllib.error.HTTPError as e:
if hasattr(e, 'code'):
    print('错误编码是' + str(e.code))
else:
print('请求成功通过。')
