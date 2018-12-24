import os
import json
import socket
import struct
import hashlib
 
sk = socket.socket()
sk.bind(('127.0.0.1', 9000))
sk.listen()
 
conn, addr = sk.accept()
filename = '[电影天堂www.dy2018.com]移动迷宫3：死亡解药BD国英双语中英双字.mp4'  # 文件名
absolute_path = os.path.join('E:\BaiduYunDownload',filename)  # 文件绝对路径
buffer_size = 1024*1024  # 缓冲大小,这里表示1MB
 
md5obj = hashlib.md5()
with open(absolute_path, 'rb') as f:
    while True:
        content = f.read(buffer_size)  # 每次读取指定字节
        if content:
            md5obj.update(content)
        else:
            break  # 当内容为空时,终止循环
 
md5 = md5obj.hexdigest()
print(md5)  # 打印md5值
 
dic = {'filename':filename,
       'filename_md5':str(md5),'buffer_size':buffer_size,
       'filesize':os.path.getsize(absolute_path)}
str_dic = json.dumps(dic).encode('utf-8')
len_dic = len(str_dic)
length = struct.pack('i', len_dic)
conn.send(length)  # dic的长度
conn.send(str_dic)  # dic
with open(absolute_path, 'rb') as f:  # 文件
    while dic['filesize']:
        content = f.read(dic['buffer_size'])
        conn.send(content)
        dic['filesize'] -= len(content)
        '''
        这里不能减等4096，因为文件，最后可能只有3字节。
        要根据读取的长度len(content),来计算才是合理的。
        '''
conn.close()
