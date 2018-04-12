
'''
# 简单socket案例

import socket

obj = socket.socket()
obj.connect(("127.0.0.1",8081))

ret = str(obj.recv(1024),encoding="utf-8")
print(ret)
'''


'''
# 机器人聊天案例

import socket
obj = socket.socket()
obj.connect(("127.0.0.1", 8080))
ret_bytes = obj.recv(1024)
ret_str = str(ret_bytes, encoding="utf-8")
print(ret_str)

while True:
    inp = input("你好请问您有什么问题? \n >>>")
    if inp == "q":
        obj.sendall(bytes(inp, encoding="utf-8"))
        break
    else:
        obj.sendall(bytes(inp, encoding="utf-8"))
        ret_bytes = obj.recv(1024)
        ret_str = str(ret_bytes, encoding="utf-8")
        print(ret_str)
'''

'''
# UDP通讯案例

import socket
ip_port = ('127.0.0.1', 9999)
sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
while True:
    inp = input('数据： ').strip()
    if inp == 'exit':
        break

    sk.sendto(bytes(inp, encoding="utf-8"), ip_port)

sk.close()
'''
