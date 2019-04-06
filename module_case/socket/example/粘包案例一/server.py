import socket
import subprocess
import struct
server = socket.socket()
ip_port = ("192.168.15.33",8001)
server.bind(ip_port)
server.listen()
conn,addr = server.accept()

while 1:
    print("等待接收消息...")
    from_client_cmd = conn.recv(1024).decode("utf-8")#接收客户端消息
    print(from_client_cmd)

    sub_obj = subprocess.Popen(   #通过subprocess模块执行服务端指令,并拿到指令结果
        from_client_cmd,            #客户端指令
        shell = True,
        stdout = subprocess.PIPE,   #标准输出:正确指令的执行结果
        stderr = subprocess.PIPE,   #标准错误输出:错误指令的执行结果
    )

    server_cmd_msg = sub_obj.stdout.read()
    #server_cmd_msg = sub_obj.stderr.read() #接收到的返回信息是bytes类型,并且windoes系统的默认编码为gbk
    cmd_msg_len = len(server_cmd_msg) #计算你要发送的数据长度
    msg_len_stru = struct.pack("i",cmd_msg_len)#先对数据长度进行打包,打包成4个字节的数据,目的是为了和你将要发送的数据拼接在一起,就像我们自制一个消息头.
    conn.send(msg_len_stru)        #首先发送打包成功后的那4个字节的数据
    conn.sendall(server_cmd_msg)   #循环send数据,直到数据全部发送成功

conn.close()
server.close()

