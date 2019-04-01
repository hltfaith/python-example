from urllib import request, error, parse

response1 = request.urlopen('https://www.python.org/')
result = response1.read().decode('utf-8')
jie = response1.geturl()
print(response1.info())
