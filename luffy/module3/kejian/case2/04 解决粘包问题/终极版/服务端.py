import socket
import subprocess
import struct
import json

phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
phone.bind(('127.0.0.1',9909)) #0-65535:0-1024给操作系统使用
phone.listen(5)

print('starting...')
while True: # 链接循环
    conn,client_addr=phone.accept()
    print(client_addr)

    while True: #通信循环
        try:
            #1、收命令
            cmd=conn.recv(8096)
            if not cmd:break #适用于linux操作系统

            #2、执行命令，拿到结果
            obj = subprocess.Popen(cmd.decode('utf-8'), shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)

            stdout=obj.stdout.read()
            stderr=obj.stderr.read()

            #3、把命令的结果返回给客户端
            #第一步：制作固定长度的报头
            header_dic={
                'filename':'a.txt',
                'md5':'xxdxxx',
                'total_size': len(stdout) + len(stderr)
            }

            header_json=json.dumps(header_dic)

            header_bytes=header_json.encode('utf-8')

            #第二步：先发送报头的长度
            conn.send(struct.pack('i',len(header_bytes)))

            #第三步：再发报头
            conn.send(header_bytes)

            #第四步：再发送真实的数据
            conn.send(stdout)
            conn.send(stderr)

        except ConnectionResetError: #适用于windows操作系统
            break
    conn.close()

phone.close()


