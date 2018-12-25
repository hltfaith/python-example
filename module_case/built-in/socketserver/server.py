import socketserver
class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            print(self.request)  # 这里不能使用input,否则卡住了
            self.request.send(b'hello')  # 跟所有的client打招呼
            print(self.request.recv(1024))  # 接收客户端的信息
if __name__ == '__main__':
    socketserver.TCPServer.allow_reuse_address = True
    server = socketserver.ThreadingTCPServer(('127.0.0.1',9000),MyServer)
    server.serve_forever()
