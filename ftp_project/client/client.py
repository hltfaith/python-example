import socket
import os,sys
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
local_home = BASE_DIR + '/client/local_home/'
user_db = BASE_DIR + '/server/db/user_db/'
sys.path.append(BASE_DIR)

from server.conf import user

def socket_conn(data):
    sk  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.connect(('127.0.0.1', 2128))

    sk.sendall(bytes(data, encoding='utf-8'))
    #print('已发------>%s', data)
    show_data = str(sk.recv(1024), encoding='utf-8')
    show = list(show_data.split(' '))

    if show[0] == '2':
        print(show[1])

    elif show[0] == '1':
        if show[1] == 'Nofile':
            print('没有找到这个文件')

        else:
            user_data = show[3]
            user_len = show[4]
            user_local = local_home + show[1] + "/" + show[2]
            with open(user_local, 'w+') as f:
                f.write(user_data)

            show_local_data = ''
            with open(user_local, 'r+') as f:
                show_local_data = f.read()

            local_data_len = str(len(show_local_data))
            if local_data_len == user_len:
                print('文件下载成功!')

            else:
                print('文件下载失败!')

    else:
        print(show_data)

def login():
    username = input('请输入您的用户名>>: ')
    password = input('请输入您的密  码>>: ')

    if os.path.exists(user_db+username+'.json'):
        user_info = {}
        with open(user_db + username + '.json', 'r+') as f:
            user_info = json.load(f)
            f.close()

        if username in user_info.keys() and user.user_encrypt(password) == user_info[username]:
            print('%s用户登录成功!' % username)
            func(username)

        else:
            print("用户名或密码输入有误!")

    else:
        print('%s用户不能存在！' % username)

def register():
    username = input('请输入您的用户名>>: ')
    password = input('请输入您的密  码>>: ')

    if os.path.exists(user_db+username+'.json'):
        print('%s用户已经注册！' % username)
    else:
        user_info = {}
        user_info[username] = user.user_encrypt(password)
        with open(user_db+username+'.json', 'w+') as f:
            json.dump(user_info, f)
            f.close()
        os.mkdir(local_home + username, 0o777)
        print('%s用户注册成功!' % username)
        func(username)

def logout():
    print("FTP程序已退出!")
    exit()

def upload(username):
    panle = '''
*******************************************
*                                         *
*  1. 上传文件 格式 为：put 空格 文件名   *
*  2. 查看 家 目录文件：ls                *
*  3. 返 回 上  一  级：bye               *
*                                         *
******************************************* 
    '''
    while True:
        choice = input('请输入命令上传文件(h)帮助>>>: ')
        user_local = local_home + username

        if choice == 'h':
            print(panle)

        elif choice == 'ls':
            for i in os.listdir(user_local):
                print(i)

        elif choice[:3] == 'put':
            file = local_home + username + '/' + choice[4:]
            if choice[4:] in os.listdir(user_local):
                data = ''
                with open(file, 'r+') as f:
                    data = f.read()
                    f.close()
                data_len = str(len(data))
                send_data = username + ' ' + 'put' + ' ' + choice[4:] + ' ' + data + ' ' + data_len
                socket_conn(send_data)

            elif choice == 'put':
                print('少参数!(h)查看帮助')

            else:
                print('该文件不存在!请重新输入')

        elif choice == 'bye':
            func(username)

        else:
            print('输入有误!(h)查看帮助')

def download(username):
    panle = '''
*********************************************
*                                           *
*  1. 下载文件 格 式  为：get 空格 文件名   *
*  2. 查看服务器目录文件：ls                *
*  3. 返  回 上  一  级 ：bye               *
*                                           *
*********************************************
    '''

    while True:
        choice = input('请输入命令下载文件(h)帮助>>>: ')

        if choice == 'h':
            print(panle)

        elif choice == 'ls':
            send_data = username + ' ' + 'show1' + ' ' + '1' + ' ' + '1' + ' ' + '1'
            socket_conn(send_data)

        elif choice[:3] == 'get':
            if choice == 'get':
                print('少参数!(h)查看帮助')

            else:
                send_data = username + ' ' + 'get' + ' ' + choice[4:] + ' ' + '1' + ' ' + '1'
                socket_conn(send_data)

        elif choice == 'bye':
            func(username)

        else:
            print('输入有误!(h)查看帮助')

def func(username):
    panle = '''
*************请选择功能****************
    1. 上传文件
    2. 下载文件
    3. 返回上一级
    '''
    num_dict = {1: upload, 2: download, 3: menu}

    while True:
        print(panle)
        choice = int(input("请输入要进入的功能编号>>>: "))
        if choice == 3:
            menu()
        elif choice in num_dict.keys():
            num_dict[choice](username)
        else:
            print("输入有误！")
            continue

def menu():

    panle = '''
*************欢迎进入ftp程序************
    1. 登录帐号
    2. 注册帐号
    3. 退出
    '''

    num_dict = {1: login, 2: register, 3: logout}
    while True:
        print(panle)
        choice = int(input("请输入要进入的功能编号>>>: ").strip())
        if choice in num_dict.keys():
            num_dict[choice]()
        else:
            print('输入有误, 请重新输入！')

if __name__ == '__main__':
    menu()
