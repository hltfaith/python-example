import socket
import struct
sk = socket.socket()
sk.connect(('127.0.0.1',9000))
count = 0
while True:
    count += 1
    msg = 'hello world'
    length = struct.pack('i',len(msg))  # 获取msg的长度，并转化为struct
    sk.send(length)  # 发送struct数据
    sk.send(msg.encode('utf-8'))  # 发送msg
    if count == 3:  # 防止死循环
        break
sk.close()
