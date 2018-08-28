import socket

phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
phone.bind(('127.0.0.1',8083)) #0-65535:0-1024给操作系统使用
phone.listen(5)

print('starting...')
while True: # 链接循环
    conn,client_addr=phone.accept()
    print(client_addr)

    while True: #通信循环
        try:
            data=conn.recv(1024)
            if not data:break #适用于linux操作系统
            print('客户端的数据',data)

            conn.send(data.upper())
        except ConnectionResetError: #适用于windows操作系统
            break
    conn.close()

phone.close()


