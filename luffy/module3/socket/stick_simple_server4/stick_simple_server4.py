import socket
import subprocess
import struct

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.bind(('127.0.0.1',9909))
phone.listen(5)

print('starting.....')

while True:
    conn, client_addr=phone.accept()
    print(client_addr)

    while True: # 通讯连接
        try:
            # 1. 收命令
            cmd = conn.recv(9909)
            if not cmd: break

            # 2. 执行命令,拿到结果
            obj = subprocess.Popen(cmd.decode('utf-8'), shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
            stdout = obj.stdout.read()
            stderr = obj.stderr.read()

            # 3. 把命令的结果返回给客户端
            #第一步：制作固定长度的报头
            total_size = len(stdout) + len(stderr)
            header = struct.pack('i', total_size)

            #第二步：把包头发送给客户端
            conn.send(header)

            #第三步：在发送真实的数据
            conn.send(stdout)
            conn.send(stderr)

        except ConnectionRefusedError:  #适用于windows操作系统
            break
    conn.close()

phone.close()
