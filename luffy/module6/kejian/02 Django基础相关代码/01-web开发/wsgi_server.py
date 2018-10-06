


from wsgiref.simple_server import make_server


def application(environ, start_response):
    # 按着http协议解析数据:environ
    # 按者http协议组装数据:start_response

    print(environ)
    print(type(environ))

    # 当前的请求路径
    path=environ.get("PATH_INFO")
    start_response('200 OK', [])

    if path=="/login":
        with open("login.html","r") as f:

            data=f.read()
    elif path=="/index":
        with open("index.html","r") as f:
            data=f.read()

    return [data.encode("utf8")]






# 封装socket
httped=make_server("",8060,application)

# 等待用户连接: conn,addr=sock.accept()
httped.serve_forever()      #  application(environ, start_response)