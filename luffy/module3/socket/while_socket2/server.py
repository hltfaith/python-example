import socket
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.setsockopt(socket.SOCK_STREAM,socket.SO_REUSEADDR, 1)

phone.bind(('127.0.0.1', 8003))
phone.listen(5)

print('string.....')
while True:   # 链接循环
    conn, client_addr = phone.accept()
    print(client_addr)

    while True: #循环通讯
        try:
            data = conn.recv(1024)
            if not data:break
            print('客户端的数据', data)

            conn.send(data.upper())

        except ConnectionRefusedError:
            break

    conn.close()
phone.close()
