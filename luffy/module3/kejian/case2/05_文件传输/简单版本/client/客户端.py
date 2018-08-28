import socket
import struct
import json

download_dir=r'/Users/linhaifeng/PycharmProjects/网络编程/05_文件传输/简单版本/client/download'

phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

phone.connect(('127.0.0.1',8912))

while True:
    #1、发命令
    cmd=input('>>: ').strip() #get a.txt
    if not cmd:continue
    phone.send(cmd.encode('utf-8'))

    #2、以写的方式打开一个新文件，接收服务端发来的文件的内容写入客户的新文件
    #第一步：先收报头的长度
    obj=phone.recv(4)
    header_size=struct.unpack('i',obj)[0]

    #第二步：再收报头
    header_bytes=phone.recv(header_size)

    #第三步：从报头中解析出对真实数据的描述信息
    header_json=header_bytes.decode('utf-8')
    header_dic=json.loads(header_json)
    '''
            header_dic={
                'filename': filename, #'filename':'1.mp4'
                'md5':'xxdxxx',
                'file_size': os.path.getsize(filename)
            }
    '''
    print(header_dic)
    total_size=header_dic['file_size']
    filename=header_dic['filename']

    #第四步：接收真实的数据
    with open('%s/%s' %(download_dir,filename),'wb') as f:
        recv_size=0
        while recv_size < total_size:
            line=phone.recv(1024) #1024是一个坑
            f.write(line)
            recv_size+=len(line)
            print('总大小：%s   已下载大小：%s' %(total_size,recv_size))


phone.close()




