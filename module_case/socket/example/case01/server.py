import socket
import time
from Prompt import Prompt
 
 
class Server(object):
    def __init__(self):
        self.ip = '127.0.0.1'
        self.port = 9999
        self.max = 1024
 
    def main(self):
        sk = socket.socket()  # 创建套接字
        sk.bind((self.ip, self.port))  # 把地址绑定到套接字
        sk.listen()  # 监听连接
        conn, addr = sk.accept()  # 等待接受客户端连接
        # print(addr)  # 打印客户端IP和端口号
        while True:
            ret = conn.recv(self.max)  # 最大接收1024字节
            msg = ret.decode('utf-8')  # 接收的信息解码
            # print(msg)  # 打印接收信息
            print(time.strftime('%Y-%m-%d %H:%M:%S'))
            print(Prompt.interlacing_color('男：' + msg))
 
            if msg.upper() == 'Q':  # 判断接收的信息是否为q
                conn.close()  # 关闭客户端套接字
                sk.close()  # 关闭服务器套接字,不再接收请求
                break  # 退出while循环
 
            content = input('>>>').strip()
            conn.send(repr(content).encode('utf-8'))  # 给客户端发送消息
 
 
if __name__ == '__main__':
    Server().main()
