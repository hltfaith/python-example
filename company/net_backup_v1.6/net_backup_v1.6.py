#-*- condig:utf-8 -*-
from netmiko import ConnectHandler
import telnetlib
import base64
import file_format
import os
import time
import re
import shutil

class login_secrt():
    # telnet_user = 'YWRtaW4='
    # telnet_secret = 'YWRtaW4xMjM='
    # ssh_user = 'YmFmYw=='
    # ssh_secret1 = 'YmFmY0AyMDE2IQ=='
    # ssh_secret2 = 'YmFmY0B4eGdsYg=='

    user = [
        'YWRtaW4=',
        'YmFmYw=='
    ]

    passwd = [
        'YWRtaW4xMjM=',
        'YmFmY0AyMDE2IQ==',
        'YmFmY0B4eGdsYg=='
    ]

    telnet_decr_user = str(base64.b64decode(user[0]), 'utf-8')
    telnet_decr_passwd = str(base64.b64decode(passwd[0]), 'utf-8')

    ssh_decr_user = str(base64.b64decode(user[1]), 'utf-8')
    ssh_decr_passwd = str(base64.b64decode(passwd[1]), 'utf-8')
    ssh_decr_passwd2 = str(base64.b64decode(passwd[2]), 'utf-8')

def telnet_login(ip):
    # 连接Telnet服务器
    print('\n')
    print('-' * 50)
    print('正连接交换机：%s' % (ip))
    tn = telnetlib.Telnet(ip, port=23, timeout=50)

    # 用于调试
    #tn.set_debuglevel(2)

    # 输入登录用户名
    login = login_secrt
    tn.read_until(b'Username:')
    tn.write(login.telnet_decr_user.encode('ascii') + b"\n")

    # 输入登录密码
    tn.read_until(b'Password:')
    tn.write(login.telnet_decr_passwd.encode('ascii') + b"\n")
    time.sleep(1)

    # 输入enable密码
    tn.write("enable".encode('ascii') + b"\n")

    time.sleep(1)
    tn.write(login.telnet_decr_passwd.encode('ascii') + b"\n")

    # 输入 show run 命令
    commands = [
        'show run'
    ]

    timestr = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    for cmd in commands:
        filename = u'%s_%s_%s.cfg' % (ip, cmd.replace(' ', '_'), timestr)
        save = open(filename, 'w')
        print('备份配置启动，正在执行命令：' + cmd)
        tn.write("show run".encode('ascii') + b"\n")

        for i in range(50):
            tn.write(b" ")
            i = i + 1
        time.sleep(5)

        result1 = tn.read_very_eager()  # 获得结果
        save.write(result1.decode('ascii'))
        save.close()

        # 删除多余行
        with open(filename, 'r') as old_file:
            line = old_file.readlines()
            for i in range(4):
                line.pop()
            save = open(filename, 'w')
            num = 1
            for i in line:
                num += 1
                if num > 9:
                    save.write(str(i))
            old_file.close()

        # 删除特殊字符
        with open(filename, 'r') as f:
            read_line = f.read()
            read_line = read_line.replace(' --More--         ', '')
            f.close()

        # 重新写入文本
        with open(filename, 'w') as fpw:
            fpw.write(read_line)
            fpw.close()
        print('%s 配置备份成功 OK !!!' % ip)
        print('-' * 50 + '\n')

    # 命令执行完毕后，终止Telnet连接（或输入exit退出）
    tn.close()

def ssh_login(ip):

    login = login_secrt

    cisco_3850 = {
        'device_type': 'cisco_ios',
        'ip': ip,
        'username': login.ssh_decr_user,
        'password':  login.ssh_decr_passwd,
        'port': 22,
        'secret': login.ssh_decr_passwd2
    }
    print('\n')
    print('-' * 50)
    print('正连接交换机：%s' % (ip))
    net_connect = ConnectHandler(**cisco_3850)
    net_connect.enable()
    commands = [
        'show run'
    ]

    timestr = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    for cmd in commands:
        filename = u'%s_%s_%s.cfg' % (ip, cmd.replace(' ', '_'), timestr)
        save = open(filename, 'w')
        print('正在执行命令：' + cmd)
        result = net_connect.send_command(cmd)
        save.write(result)
        print('%s 配置备份成功 OK !!!' % ip)
        print('-' * 50 + '\n')
    net_connect.disconnect()

if __name__ == '__main__':

    while True:
        print('''
        序号 
         1.  配置备份
         2.  备份文件格式装换
         3.  退出 (q)
        ''')
        choice = int(input('请选择：'))
        if choice == 1:
            telnet = [
                '172.16.100.16',
                '172.16.100.17',
                '172.16.100.18',
                '172.16.100.19'
            ]

            ssh = [
                '172.16.101.1',
                '172.16.100.15'
            ]
            starttime = time.time()
            current_month = os.getcwd() + "\\" + time.strftime('%Y-%m-%d')

            if not os.path.exists(current_month):
                os.mkdir(current_month)

            for ip in telnet:
                telnet_login(ip)

            for ip in ssh:
                ssh_login(ip)

            all_files = os.listdir(os.curdir)
            for i in all_files:
                if re.findall('\.cfg', i):
                    shutil.move(i, current_month)
            endtime = time.time()

            print('******************************************************************************\n')
            print('备份结果路径在 %s 中! \n' % (current_month))
            print('请选择文件格式装换功能，进行更改文件编码')
            print('备份所用时间 %s 秒\n' % int(endtime - starttime))
            print('******************************************************************************')
            continue

        elif choice == 2:
            file_format.rename()

        elif choice == 3:
            exit()

        else:
            print('输入错误，重新输入！')
