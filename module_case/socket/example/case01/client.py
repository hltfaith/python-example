import socket
import time
from Prompt import Prompt
 
 
class Client(object):
    def __init__(self):
        self.ip = '127.0.0.1'
        self.port = 9999
        self.max = 1024
 
    def main(self):
        sk = socket.socket()  # 创建客户套接字
        sk.connect((self.ip, self.port))  # 尝试连接服务器
        while True:
            content = input('>>>').strip()
            sk.send(repr(content).encode('utf-8'))  # 发送数据
 
            ret = sk.recv(self.max)  # 最大接收1024字节
            msg = ret.decode('utf-8')  # 接收的信息解码
            # print(msg)  # 打印接收信息
            print(time.strftime('%Y-%m-%d %H:%M:%S'))
            print(Prompt.interlacing_color('女：' + msg))
 
            if content.upper() == 'Q':  # 判断接收的信息是否为q
                sk.send(repr(content).encode('utf-8'))  # 发送q给服务器
                sk.close()  # 关闭客户套接字
                break  # 跳出while循环
 
 
if __name__ == '__main__':
    Client().main()
