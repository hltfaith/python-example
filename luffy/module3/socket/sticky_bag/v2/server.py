import socket, json
import subprocess

ip_port = ('127.0.0.1', 8080)

tcp_socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # 一行代码搞定，写在bind之前
tcp_socket_server.bind(ip_port)
tcp_socket_server.listen(5)

def pack_msg_header(header,size):
    bytes_header = bytes(json.dumps(header),encoding="utf-8")
    fill_up_size = size -  len(bytes_header)
    print("need to fill up ",fill_up_size)

    header['fill'] = header['fill'].zfill(fill_up_size)
    print("new header",header)
    bytes_new_header = bytes(bytes(json.dumps(header),encoding="utf-8"))
    return bytes_new_header

while True:
    conn, addr = tcp_socket_server.accept()
    print('客户端', addr)

    while True:
        cmd = conn.recv(1024)
        if len(cmd) == 0: break
        print("recv cmd",cmd)
        res = subprocess.Popen(cmd.decode('utf-8'), shell=True,
                               stdout=subprocess.PIPE,
                               stdin=subprocess.PIPE,
                               stderr=subprocess.PIPE)

        stderr = res.stderr.read()
        stdout = res.stdout.read()
        print("res length",len(stdout))

        msg_header = {
            'length':len(stdout + stderr),
            'fill':''
        }
        packed_header = pack_msg_header(msg_header, 100)
        print("packed header size", packed_header, len(packed_header))
        conn.send(packed_header)
        conn.send(stdout + stderr)



'''
文艺青年版一
思考一个问题，为什么不能在发送了消息长度(称为消息头head吧)给对端后，立刻发消息内容(称为body吧)，是因为怕head 和body 粘在一起，
所以通过等对端返回确认来把两条消息中断开。

可不可以直接发head + body,但又能让对端区分出哪个是head，哪个是body呢？我靠、我靠，感觉智商要涨了。

想到了，把head设置成定长的呀，这样对端只要收消息时，先固定收定长的数据，head里写好，后面还有多少是属于
这条消息的数据，然后直接写个循环收下来不就完了嘛！唉呀妈呀，我真机智。

可是、可是如何制作定长的消息头呢？假设你有2条消息要发送，第一条消息长度是 3000个字节，第2条消息是200字节。如果消息头只包含消息长
度的话，那两个消息的消息头分别是

len(msg1) = 4000 = 4字节
len(msg2) = 200 = 3字节
你的服务端如何完整的收到这个消息头呢？是recv(3)还是recv(4)服务器端怎么知道？用尽我所有知识，我只能想到拼接字符串的办法了，打比方就
是设置消息头固定100字节长，不够的拿空字符串去拼接。

'''
