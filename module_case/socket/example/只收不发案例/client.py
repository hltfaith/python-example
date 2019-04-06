import socket

ip_port = ('47.98.125.53', 8080)

sk = socket.socket()
sk.connect(ip_port)

welcom_msg = sk.recv(200).decode()
print(welcom_msg)

while True:
    send_data = input(">>: ").strip()

    if send_data == 'exit': break
    if len(send_data) == 0: continue

    # 判断数据包大小
    if len(send_data) <= 1024:
        sk.send(bytes(send_data, encoding='utf8'))
        break
    else:
        print('pack size out!!!')


    # 基于已经收到的接待收数据长度
    # recv_size = 0
    # recv_msg = b''
    # while recv_size < msg_size:
    #     recv_data = sk.recv(1024)
    #     recv_msg += recv_data
    #     recv_size += len(recv_data)
    #
    #     print('MSG SIZE %s RECE SIZE %s' %(msg_size, recv_size))
    # print(str(recv_msg, encoding='utf8'))

sk.close()
