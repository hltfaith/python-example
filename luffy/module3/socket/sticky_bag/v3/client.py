from socket import *
import struct,json

ip_port = ('127.0.0.1', 8080)
client = socket(AF_INET, SOCK_STREAM)
client.connect(ip_port)

while True:
    cmd = input('>>: ')
    if not cmd: continue
    client.send(bytes(cmd, encoding='utf-8'))

    head = client.recv(4) #先收4个bytes，这里4个bytes里包含了报头的长度
    head_json_len=struct.unpack('i',head)[0] #解出报头的长度
    head_json=json.loads(client.recv(head_json_len).decode('utf-8')) #拿到报头
    data_len=head_json['data_size'] #取出报头内包含的信息

    #开始收数据
    recv_size=0
    recv_data=b''
    while recv_size < data_len:
        recv_data+=client.recv(1024)
        recv_size+=len(recv_data)

    print(recv_data.decode('utf-8'))
    #print(recv_data.decode('gbk')) #windows默认gbk编码
