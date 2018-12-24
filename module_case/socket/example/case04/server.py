import os
import json
import struct
import socket
import hashlib
 
sk = socket.socket()
sk.bind(('127.0.0.1',9999))
sk.listen()
 
conn,addr = sk.accept()
print(addr)
 
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
 
dic = {'filename':filename, 'filename_md5':str(md5),'buffer_size':buffer_size,
       'filesize':os.path.getsize(absolute_path)}
str_dic = json.dumps(dic).encode('utf-8')  # 将字典转换为json
dic_len = struct.pack('i', len(str_dic))  # 获取字典长度,转换为struct
conn.send(dic_len)  # 发送字典长度
conn.send(str_dic)  # 发送字典
 
with open(absolute_path, 'rb') as f:  # 打开文件
    while True:
        content = f.read(buffer_size)  # 每次读取指定大小的字节
        if content:  # 判断内容不为空
            conn.send(content)  # 每次读取指定大小的字节
        else:
            break
             
conn.close()  # 关闭连接
sk.close()  # 关闭套接字
