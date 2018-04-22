import socket,time
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
res=s.connect_ex(('127.0.0.1',8080))

while True:
    msg=input('>>: ').strip()
    if len(msg) == 0:continue
    if msg == 'quit':break

    s.send(msg.encode('utf-8'))
    length=int(s.recv(1024).decode('utf-8'))
    s.send('recv_ready'.encode('utf-8'))
    send_size=0
    recv_size=0
    data=b''
    while recv_size < length:
        data+=s.recv(1024)
        recv_size+=len(data) #为什么不直接写1024？


    print(data.decode('utf-8'))

# 为何low？
#
# 程序的运行速度远快于网络传输速度，所以在发送一段字节前，先用send去发送该字节流长度，这种方式会放大网络延迟带来的性能损耗
# 刚才上面 在发送消息之前需先发送消息长度给对端，还必须要等对端返回一个ready收消息的确认，不等到对端确认就直接发消息的话，还
# 是会产生粘包问题(承载消息长度的那条消息和消息本身粘在一起)。 有没有优化的好办法么？
