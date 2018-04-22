import socket

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

while True:

    msg = input(">>>:").strip()
    if len(msg) == 0:continue

    client.sendall(msg.encode()) #发送用户输入的数据,必须是bytes模式

    data = client.recv(1024)

    print('Received',data.decode()) #收到服务器的响应后，decode一下
