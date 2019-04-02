from urllib import request, error, parse

# headers 信息，从fiddler上或你的浏览器上可复制下来
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

# POST请求的信息，填写你的用户名和密码
value = {

    'source': 'index_nav',
    'username': 'your name',
    'password': 'your passwd'

}

try:

    data = parse.urlencode(value).encode('utf8')
    response = request.Request('https://www.douban.com', data=data, headers=headers)
    html = request.urlopen(response)
    result = html.read().decode('utf8')
    print(result)

except error.URLError as e:
    if hasattr(e, 'reason'):
        print('错误原因是' + str(e.reason))

except error.HTTPError as e:
    if hasattr(e, 'code'):
        print('错误编码是' + str(e.code))
    else:
        print('请求成功通过')
