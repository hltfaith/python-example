
from wsgiref.simple_server import make_server




def application(environ, start_response):

    start_response('200 OK', [('Content-Type', 'text/html'),("Charset","utf8")])

    print("PATH",environ.get("PATH_INFO"))

    # 当前请求路径
    path=environ.get("PATH_INFO")

    # 方案1:
    # if path=="/favicon.ico":
    #
    #     with open("favicon.ico","rb") as f:
    #         data=f.read()
    #     return [data]
    #
    # elif path=="/login":
    #      with open("login.html","rb") as f:
    #         data=f.read()
    #      return [data]
    #
    # elif path=="/index":
    #      with open("index.html","rb") as f:
    #         data=f.read()
    #      return [data]
    # 方案2:

    from urls import url_patterns

    func=None
    for item in url_patterns:
        if path==item[0]:
            func=item[1]
            break

    if func:
        return [func(environ)]

    else:
        return [b'404!']


httpd = make_server('', 9988, application)

# 开始监听HTTP请求:
httpd.serve_forever()