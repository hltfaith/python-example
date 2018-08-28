import socket
import time

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(('127.0.0.1',9904))


client.send('hello'.encode('utf-8'))
time.sleep(5)
client.send('world'.encode('utf-8'))
