import json
import struct
import socket
 
sk = socket.socket()
sk.connect(('127.0.0.1',9000))
 
dic_len = sk.recv(4)
dic_len = struct.unpack('i',dic_len)[0]
str_dic = sk.recv(dic_len).decode('utf-8')
dic = json.loads(str_dic)
 
with open(dic['filename'],'wb') as f:
    content = sk.recv(dic['filesize'])
    f.write(content)
sk.close()
