import socket
import time
import shutil
import re
import os

cap_path = "E:\\"

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('192.168.3.23', 18888))
socket.listen(5)
print('start......')

# BF-A211532000
# BF-A211532000_A0310_00155___CAP_1_-1_report.doc

def local_filelist(data):
    cap_all_file = os.listdir(cap_path)
    #print(cap_all_file)
    data = data.split(',')

    for i in data:
        i = i + '_A0310'
        for k in cap_all_file:
            if re.findall(i+'*', k):
                print(k)

def exc_server():

    while True:
        conn, addr = socket.accept()

        while True:

            try:
                data = conn.recv(10240)
                if not data:break

                data = data.decode('utf-8')
                print('客户端数据', data)
                local_filelist(data)



                conn.send('test success data !!!'.encode('utf-8'))
                time.sleep(3)
                conn.send('exit'.encode('utf-8'))

            except ConnectionResetError:
                break

        conn.close()

# socket.close()

if __name__ == '__main__':
    exc_server()
