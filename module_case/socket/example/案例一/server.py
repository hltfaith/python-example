import socket
import subprocess

ip_port = ('127.0.0.1', 9999)

# 买手机
s = socket.socket()  # 绑定协议，生成套接字
s.bind(ip_port)      # 绑定ip+协议+端口：用来唯一标识一个进程，ip_port必须是元组格式
s.listen(5)          # 定义最大可以挂起链接数

# 等待电话
while True:  # 用来重复接收新的链接
    conn, addr = s.accept()   # 接收客户端胡的接请求，返回conn（相当于一个特定胡链接），addr是客户端ip+port
    conn.sendall(bytes('欢迎致电 10086，请输入1xxx,0转人工服务.', encoding='utf-8'))

    # 收消息
    while True: # 用来基于一个链接重复收发消息
            try: # 捕捉客户端异常关闭（ctrl+c）
                recv_data = conn.recv(1024) # 收消息，阻塞
                if len(recv_data) == 0: break # 客户端如果退出，服务端将收到空消息，退出

                # 发消息
                p=subprocess.Popen(str(recv_data,encoding='utf8'),shell=True,stdout=subprocess.PIPE) # 执行系统命令，windows平
                                                                                                      # 台命令的标准输出是gbk编码，需要转换
                res=p.stdout.read()   # 获取标准输出
                if len(res) == 0:   # 执行错误命令，标准输出为空，
                    send_data='cmd err'
                # else:
                #     send_data=str(res,encoding='gbk')  # 命令执行ok，字节gbk---->str---->字节utf-8
                print(str)
                send_data=bytes(str(res, encoding='utf8'), encoding='utf8')


                # 解决粘包问题
                ready_tag='Ready|%s' % len(send_data)
                conn.send(bytes(ready_tag, encoding='utf8')) # 发送数据长度
                feedback=conn.recv(1024)  # 接收确认信息
                feedback=str(feedback, encoding='utf8')

                if feedback.startswith('Start'):
                    conn.send(send_data)  # 发送命令的执行结果
            except Exception:
                break
    #挂电话
    conn.close()
