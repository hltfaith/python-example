import socket
import time

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.0.0.1',9904)) #0-65535:0-1024给操作系统使用
server.listen(5)


conn,addr=server.accept()

#第一次接收:5
# res1=conn.recv(1) #b'hello'
# res2=conn.recv(1) #b'hello'
# res3=conn.recv(1) #b'hello'
# res4=conn.recv(1) #b'hello'
# res5=conn.recv(1) #b'hello'
# print('第一次',res1+res2+res3+res4+res5) #b'h'
res1=conn.recv(5) #world
print(res1)
time.sleep(6)


#第二次接收:5
res1=conn.recv(2) #world
res2=conn.recv(3) #world
print('第二次',res1+res2)