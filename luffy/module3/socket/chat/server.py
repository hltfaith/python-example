import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port

sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_server.bind((HOST, PORT))

sock_server.listen(1)     #开始监听，1代表在允许有一个连接排队，更多的新连接连进来时就会被拒绝
conn, addr = sock_server.accept() #阻塞直到有连接为止，有了一个新连接进来后，就会为这个请求生成一个连接对象

with conn:
    print('Connected by', addr)
    while True:
        data = conn.recv(1024) #接收1024个字节
        print("recv from Alex:",conn.getpeername(), data.decode())
        if not data: break #收不到数据，就break

        response = input(">>>").strip()
        conn.send(response.encode())
        print("send to alex:",response)
