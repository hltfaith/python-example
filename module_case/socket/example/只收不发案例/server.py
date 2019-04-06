#coding:utf-8
'''

    实现需求

    1. server 端只收不发

          1).收包流程
              粘包

              解包

              头信息
                Key号:   密码
                ID号：   唯一标识符
                状态：
                地址：
                类型：
                长度：
                数据：

'''

import socket

ip_port = ('0.0.0.0', 8080)
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
sk.bind(ip_port)
sk.listen(5)

print('Ncoreqp分布式抢票系统启动成功')
print('监听端口：8080')
print('........')

while True:
    conn, addr = sk.accept()
    conn.sendall(bytes('欢迎使用Ncoreqp分布式抢票系统'))

    while True:


            recv_data = conn.recv(1024)
            if len(recv_data) == 0: break

            print('recv pack: %s' % str(recv_data))

            # p = subprocess.Popen(str(recv_data, encoding='utf-8'), shell=True, stdout=subprocess.PIPE)
            # res = p.stdout.read()
            # if len(res) == 0:
            #     send_data = 'cmd err'
            #
            # print(str)
            # send_data = bytes(str(res, encoding='utf8'), encoding='utf8')


            # 解决粘包问题
            # ready_tag = 'Ready|%s' % len(send_data)
            # conn.send(bytes(ready_tag, encoding='utf8'))
            #
            # feedback = conn.recv(1024)
            # feedback = str(feedback, encoding='utf8')
            #
            # if feedback.startswith('Start'):
            #     conn.send(send_data)
