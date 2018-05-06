'''
from socket import *
from threading import Thread

def communicate(conn):
    while True:
        try:
            data = conn.recv(1024)
            if not data: break
            conn.send(data.upper())
        except ConnectionResetError:
            break

def server(ip, port):
    server = socket(AF_INET, SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)

    while True:
        conn, addr = server.accept()
        t = Thread(target=communicate, args=(conn,))
        t.start()

if __name__ == '__main__':
    server('127.0.0.1', 8082)

'''

# 基于线程池实现

from socket import *
from concurrent.futures import ThreadPoolExecutor

def communicate(conn):
    while True:
        try:
            data = conn.recv(1024)
            if not data: break
            conn.send(data.upper())
        except ConnectionResetError:
            break

    conn.close()

def server(ip, port):
    server = socket(AF_INET, SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)

    while True:
        conn, addr = server.accept()
        pool.submit(communicate, conn)

    server.close()


if __name__ == '__main__':
    pool = ThreadPoolExecutor(2)
    server('127.0.0.1', 8083)

