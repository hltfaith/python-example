import socket
sk = socket.socket()
sk.connect(('127.0.0.1',9000))
while True:
    print(sk.recv(1024))
    #inp = input('>>>').encode('utf-8')
    sk.send(b'hahaha')
sk.close()
