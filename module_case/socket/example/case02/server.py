import struct
import socket
 
sk = socket.socket()
sk.bind(('127.0.0.1',9000))
sk.listen()
 
conn,addr = sk.accept()
count = 0
while True:
    count += 1
    ret = conn.recv(4)  # int类型的struct长度固定为4字节
    #print(ret)
    length = struct.unpack('i',ret)[0]  #反解struct数据,取元组第一个值
    msg = conn.recv(length)  # 接收指定字节
    print(msg.decode('utf-8'))  # 打印接收信息
    if count == 3:  # 防止死循环
        break
conn.close()
