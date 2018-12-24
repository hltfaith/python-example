import json
import struct
import socket
import sys
import time
import hashlib
import os
from Prompt import Prompt
 
def processBar(num, total):  # 进度条
    rate = num / total
    rate_num = int(rate * 100)
    pretty = Prompt.random_color('✈')
    if rate_num == 100:
        r = '\r{}{}%\n'.format(pretty * int(rate_num / 5), rate_num,)
    else:
        r = '\r{}{}%'.format(pretty * int(rate_num / 5), rate_num,)
    sys.stdout.write(r)
    sys.stdout.flush
 
start_time = time.time()  # 开始时间
 
sk = socket.socket()
sk.connect(('127.0.0.1',9000))
 
dic_len = sk.recv(4)
dic_len = struct.unpack('i',dic_len)[0]
dic = sk.recv(dic_len)
str_dic = dic.decode('utf-8')
dic = json.loads(str_dic)
 
md5 = hashlib.md5()
with open(dic['filename'],'wb') as f:  # 使用wb更严谨一些,虽然可以使用ab
    content_size = 0
    while True:
        content = sk.recv(dic['buffer_size'])  # 接收指定大小
        f.write(content)  # 写入文件
        content_size += len(content)  # 接收大小
        md5.update(content)  # 摘要
 
        processBar(content_size,dic['filesize'])  # 执行进度条函数
        if content_size == dic['filesize']:break  # 当接收的总大小等于文件大小时,终止循环
 
    md5 = md5.hexdigest()
    print(md5)  # 打印md5值
    if dic['filename_md5'] == str(md5):
        print(Prompt.display('md5校验正确--下载成功','green'))
    else:
        print(Prompt.display('文件验证失败', 'red'))
        os.remove(dic['filename'])  # 删除文件
 
sk.close()  # 关闭连接
 
end_time = time.time()  # 结束时间
print('本次下载花费了{}秒'.format(end_time - start_time))
