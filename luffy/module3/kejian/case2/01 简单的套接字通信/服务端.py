import socket

#1、买手机
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# print(phone)

#2、绑定手机卡
phone.bind(('127.0.0.1',8081)) #0-65535:0-1024给操作系统使用

#3、开机
phone.listen(5)

#4、等电话链接
print('starting...')
conn,client_addr=phone.accept()

#5、收，发消息
data=conn.recv(1024) #1、单位：bytes 2、1024代表最大接收1024个bytes
print('客户端的数据',data)

conn.send(data.upper())

#6、挂电话
conn.close()

#7、关机
phone.close()