import socket
import struct
import json
import os
tcp_server = socket.socket()
ip_port = ('127.0.0.1',8001)#本机回环地址,供内部程序之间测试用
tcp_server.bind(ip_port)
tcp_server.listen()
client_file_path = r'F:\pp'

conn,adddr = tcp_server.accept()
file_info_stru = conn.recv(4)#首先接收到文件信息长度转换出来的4个字节的数据
file_info_len = struct.unpack('i',file_info_stru)[0]#解包文件信息的长度
client_file_info = conn.recv(file_info_len).decode('utf-8')
abc_file_info = json.loads(client_file_info)#将接收到的json字符串反序列化
print('abc_file_info>>>',abc_file_info)
client_file_size = abc_file_info['file_size']

recv_all_size = 0
client_full_path = client_file_path + '\\' + abc_file_info['file_name']
# client_full_path = os.path.join(client_file_path,abc_file_info['file_name'])
with open(client_full_path,'wb') as f:
    while recv_all_size < client_file_size:
        every_recv_data = conn.recv(1024)
        f.write(every_recv_data)
        recv_all_size += len(every_recv_data)


conn.send('小伙牛逼啊,上传成功!'.encode('utf-8'))
conn.close()
tcp_server.close()

