import json
import struct
import socket
import hashlib
import time
 
start_time = time.time()
sk = socket.socket()
sk.connect(('127.0.0.1',9999))
 
dic_len = sk.recv(4)  # 接收4字节,因为struct的int为4字节
dic_len = struct.unpack('i',dic_len)[0]  # 反解struct得到元组，获取元组第一个元素
#print(dic_len)  # 返回一个数字
str_dic = sk.recv(dic_len).decode('utf-8')  # 接收指定长度,获取完整的字典,并解码
#print(str_dic)  # json类型的字典
dic = json.loads(str_dic)  # 反序列化得到真正的字典
#print(dic)  # 返回字典
 
md5 = hashlib.md5()
with open(dic['filename'],'wb') as f:
    while True:
        content = sk.recv(dic['buffer_size'])
        if not content:
            break
        md5.update(content)
    md5 = md5.hexdigest()
    print(md5)  # 打印md5值
 
    if dic['filename_md5'] == str(md5):
        f.write(content)
        print('md5校验正确--下载成功')
    else:
        print('文件验证失败')
 
sk.close()
 
end_time = time.time()
print('本次下载花费了{}秒'.format(end_time-start_time))
