'''
#简单socket案例

import socket

sk = socket.socket()
sk.bind(("127.0.0.1",8081))
sk.listen(5)

conn, address = sk.accept()
conn.sendall(bytes("Hello world",encoding="utf-8"))
'''


'''
#机器人案例 

import socketserver
class Myserver(socketserver.BaseRequestHandler):

    def handle(self):
        conn = self.request
        conn.sendall(bytes("你好,我是机器人", encoding="utf-8"))
        while True:
            ret_bytes = conn.recv(1024)
            ret_str = str(ret_bytes, encoding="utf-8")
            if ret_str == "q":
                break
            conn.sendall(bytes(ret_str+"你好我好大家好", encoding="utf-8"))


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(("127.0.0.1", 8080), Myserver)
    server.serve_forever()
'''

'''
# UDP通讯案例

import socket
ip_port = ('127.0.0.1', 9999)
sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

sk.bind(ip_port)
while True:
    data = sk.recv(1024)
    print(data)
'''


'''
# WEB应用案例

import socket

def handle_request(client):
    buf = client.recv(1024)
    buf.send('HTTP/1.1 200 OK\r\n\r\n')
    buf.send("Hello, World")

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', 8080))
    sock.listen(5)

    while True:
        conn, address = sock.accept()
        handle_request(conn)
        conn.close()

if __name__ == '__main__':
    main()
'''
