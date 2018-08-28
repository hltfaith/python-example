# from socket import *
#
# server=socket(AF_INET,SOCK_DGRAM)
# server.bind(('127.0.0.1',8080))
#
#
# res1=server.recvfrom(1024)
# print('第一次：',res1)
#
# res2=server.recvfrom(1024)
# print('第二次：',res2)
#
#
# server.close()



from socket import *

server=socket(AF_INET,SOCK_DGRAM)
server.bind(('127.0.0.1',8080))


res1=server.recvfrom(1) #b'hello'
print('第一次：',res1)

res2=server.recvfrom(1024) #b'world'
print('第二次：',res2)


server.close()