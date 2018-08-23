import socket
import time

link_ch = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
link_ch.connect(('192.168.3.23', 18888))

def export():
    msg = input('请输入要抽取合同编号：').strip()
    link_ch.send(msg.encode('utf-8'))
    time.sleep(2)
    print('正在导出请稍等......')

    while True:
        data = link_ch.recv(10240)
        data = data.decode('utf-8')

        if data == 'exit':
            print('合同已导出到本地,请查阅！！！')
            exit()

        elif data == '':
            pass

        else:
            print(data)


if __name__ == '__main__':
    export()
