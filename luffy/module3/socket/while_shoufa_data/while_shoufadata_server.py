import socket
socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = ''
PORT = 50007
socket_server.bind((HOST, PORT))
socket_server.listen(1)
conn, addr = socket_server.accept()

while conn:
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        print("server recv:" ,conn.getpeername(), data.decode())
        if not data: break
        conn.sendall(data)
