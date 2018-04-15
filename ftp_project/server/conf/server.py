import socketserver
import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
user_home = BASE_DIR + '/db/user_home/'
sys.path.append(BASE_DIR)

import user

class myserver(socketserver.BaseRequestHandler):
    print('服务启动....')
    def handle(self):

        conn = self.request
        print('监听程序--->%s' % conn)

        while True:
            show = str(conn.recv(1024), encoding='utf-8')
            print(show)
            user_list = show.split(' ')
            username = user_list[0]
            func = user_list[1]
            filename = user_list[2]
            filedata = user_list[3]
            file_len = user_list[4]

            if len(show) == 0:
                print('已收--->', show, '空值')
                conn.sendall(bytes('hui > ' + show + '空值', encoding='utf-8'))
                continue

            elif func == 'put':
                return_tag = user.user_data(username, filename, filedata, file_len).upload()
                print(return_tag + "   <----已收")
                return_tag1 = return_tag + ' ' + ' ' + ' ' + ' ' + ' ' + ' ' + ' ' + ' '
                conn.sendall(bytes(return_tag1, encoding='utf-8'))

            elif func == 'show1':
                return_tag = user.user_data(username, filename, filedata, file_len).show_list()
                print(return_tag+"   <----已收")
                return_tag1 = '2' + ' ' + return_tag + ' ' + '1' + ' ' + '1' + ' ' + '1'
                conn.sendall(bytes(return_tag1, encoding='utf-8'))

            elif func == 'get':
                return_tag = user.user_data(username, filename, filedata, file_len).download()
                print(return_tag + "   <----已收")
                return_tag1 = '1' + ' ' + return_tag
                conn.sendall(bytes(return_tag1, encoding='utf-8'))

            else:
                conn.sendall(bytes(' %s server is show success' % show, encoding='utf-8'))
                break

if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 2128), myserver)
    server.serve_forever()
