

import socket

sock=socket.socket()
sock.bind(("127.0.0.1",9998))
sock.listen(5)

while 1:

    print("server waiting.....")
    conn,addr=sock.accept()
    data=conn.recv(1024)  #  ---------dict/obj     d={"path":"/login"}
    print(data)

    #d.get("path")

    # 按着http请求协议解析数据

    # 专注与web业务开发
    # path=d.get("path")
    #
    # if path=="/login":
    #     return login.html

    # 按着http响应协议封装数据



    # 读取html文件
    with open("index.html","rb") as f:
        data=f.read()

    conn.send((b"HTTP/1.1 200 OK\r\n\r\n%s"%data))
    conn.close()

'''

请求首行
请求头
请求头
请求头
请求头
....

请求体(a=1&b=2)  # 注意:只有POST请求才会有请求体

b'GET / HTTP/1.1\r\nHost: 127.0.0.1:8880\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: zh-CN,zh;q=0.9,en;q=0.8\r\nCookie: csrftoken=IU9cIEWdRzTx7gm6JIjASm9TZJSve8jUGcfXPbgTXpSW0iHot1NOxpjdroESRB4f\r\n\r\n'
b'GET /yuan?name=yuan&age=22 HTTP/1.1\r\nHost: 127.0.0.1:8880\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: zh-CN,zh;q=0.9,en;q=0.8\r\nCookie: csrftoken=IU9cIEWdRzTx7gm6JIjASm9TZJSve8jUGcfXPbgTXpSW0iHot1NOxpjdroESRB4f\r\n\r\n'
b'POST / HTTP/1.1\r\nHost: 127.0.0.1:8880\r\nConnection: keep-alive\r\nContent-Length: 20\r\nPragma: no-cache\r\nCache-Control: no-cache\r\nOrigin: http://127.0.0.1:8880\r\nUpgrade-Insecure-Requests: 1\r\nContent-Type: application/x-www-form-urlencoded\r\nUser-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\nReferer: http://127.0.0.1:8880/\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: zh-CN,zh;q=0.9,en;q=0.8\r\nCookie: csrftoken=IU9cIEWdRzTx7gm6JIjASm9TZJSve8jUGcfXPbgTXpSW0iHot1NOxpjdroESRB4f\r\n\r\nuser=bisheng&pwd=456'


URL:

协议://IP:端口(80)/路径?a=1&b=2


'''


















