import socket
import struct
client = socket.socket()
server_ip_port = ("192.168.15.33",8001)
client.connect(server_ip_port)

while 1:
    msg = input("请输入要执行的命令>>>>>")
    client.send(msg.encode("utf-8"))

    from_server_msglen = client.recv(4)#先接受服务端要发送给我的数据长度,前四个字节,固定的
    unpack_len_msg = struct.unpack("i",from_server_msglen)[0]

    recv_msg_len = 0
    all_msg = b""
    while recv_msg_len < unpack_len_msg:
        every_recv_date = client.recv(1024)
        all_msg += every_recv_date  #将每次接收到的数据进行拼接和统计
        recv_msg_len += len(every_recv_date) #对每次接受到的数据进行累加

    print(all_msg.decode("gbk"))
client.close()

