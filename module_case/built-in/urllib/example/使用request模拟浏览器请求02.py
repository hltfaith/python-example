from urllib import request, error, parse

# 使用request 模拟浏览器请求 python.org网站

headers = {'User_Agent': ''}
response = request.Request('https://www.python.org/', headers=headers)
html = request.urlopen(response)
result = html.read().decode('utf-8')
print(result)

