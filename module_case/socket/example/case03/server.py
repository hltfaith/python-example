import os
import json
import struct
import socket
 
# E:\BaiduYunDownload\AppleEthernet-master.zip
sk = socket.socket()
sk.bind(('127.0.0.1',9000))
sk.listen()
 
conn,addr = sk.accept()
print(addr)
dic = {'filename':'AppleEthernet-master.zip',
       'filesize':os.path.getsize(r'E:\BaiduYunDownload\AppleEthernet-master.zip')}
str_dic = json.dumps(dic).encode('utf-8')
dic_len = struct.pack('i',len(str_dic))
conn.send(dic_len)
conn.send(str_dic)
with open(r'E:\BaiduYunDownload\AppleEthernet-master.zip','rb') as f:
    content = f.read()
conn.send(content)
conn.close()
sk.close()
