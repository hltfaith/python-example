import socket
import struct
import json
import os
tcp_client = socket.socket()
server_client = socket.socket()
server_ip_port = ("127.0.0.1",8001)
tcp_client.connect(server_ip_port)
read_size = 1024

file_info = {
    'file_path':r'F:\untitled\10.18\jj\aaa.mp4',
    'file_name':'aaa.mp4',
    'file_size':None,
}
file_size = os.path.getsize(file_info["file_path"])#获取文件大小
file_info["file_size"] = file_size#将文件大小添加到文件信息的字典中
file_info_json = json.dumps(file_info)#因为我们要发送的数据是字节类型,那么必须将字典转换为bytes类型,但字典不能直接转换为byte,所以用过先转换成字符串
file_info_len = len(file_info_json) #获取字符串的长度
file_info_stru = struct.pack("i",file_info_len)#将长度打包为四个字节
tcp_client.send(file_info_stru)#将打包好的4个自己的数据和我的文件信息数据一起发送给了服务端
tcp_client.send(file_info_json.encode("utf-8"))

all_file_data = b'' #统计文件数据
all_size_len = 0    #统计文件数据长度

with open(file_info['file_path'],'rb') as f:
    while all_size_len < file_size:
        every_read_data = f.read(read_size)
        all_file_data += every_read_data
        all_size_len += len(every_read_data)
        tcp_client.send(every_read_data)#发送每次读取的数据

print(tcp_client.recv(1024).decode('utf-8'))
tcp_client.close()

