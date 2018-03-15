import socket
import subprocess

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.bind(('127.0.0.1', 9901))
phone.listen(5)

print('starting....')
while True:
    conn, client_addr = phone.accept()
    print(client_addr)

    while True: # 通讯循环
        try:
            #1. 收命令
            cmd = conn.recv(1024)
            if not cmd: break

            #2. 执行命令，拿到结果
            obj = subprocess.Popen(cmd.decode('utf-8'), shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
            stdout=obj.stdout.read()
            stderr=obj.stderr.read()

            #3. 把命令的结果返回的客户端
            print(len(stdout)+len(stderr))
            conn.send(stdout+stderr)

        except ConnectionRefusedError:
            break

    conn.close()

phone.close()
