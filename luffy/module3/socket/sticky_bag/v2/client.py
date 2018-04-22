import socket
import json

ip_port = ('127.0.0.1', 8080)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
res = s.connect_ex(ip_port)

while True:
    msg = input('>>: ').strip()
    if len(msg) == 0: continue
    if msg == 'quit': break

    s.send(msg.encode('utf-8'))
    response_msg_header = s.recv(100).decode("utf-8")

    response_msg_header_data = json.loads(response_msg_header)
    msg_size = response_msg_header_data['length']

    res = s.recv(msg_size)
    print("received res size ", len(res))
    print(res.decode('utf-8'), end='')
