import socket

phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

phone.connect(('127.0.0.1',8083))

while True:
    msg=input('>>: ').strip() #msg=''
    if not msg:continue
    phone.send(msg.encode('utf-8')) #phone.send(b'')
    # print('has send')
    data=phone.recv(1024)
    # print('has recv')
    print(data.decode('utf-8'))

phone.close()