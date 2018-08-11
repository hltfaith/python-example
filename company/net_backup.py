#-*- condig:utf-8 -*-
from netmiko import ConnectHandler
import telnetlib
import time
import base64

telnet_user = 'MTIz'
telnet_secret = 'MTIz'
telnet_decr = str(base64.b64decode(telnet_secret), 'utf-8')
telnet_decr_user = str(base64.b64decode(telnet_user), 'utf-8')

def telnet_login(ip):
    # 连接Telnet服务器
    print('\n')
    print('-' * 50)
    print('正连接交换机：%s' % (ip))
    tn = telnetlib.Telnet(ip, port=23, timeout=50)
    # 输入登录用户名
    tn.read_until(b'Username:')
    tn.write(telnet_decr_user.encode('ascii') + b"\n")

    # 输入登录密码
    tn.read_until(b'Password:')
    tn.write(telnet_decr.encode('ascii') + b"\n")
    time.sleep(1)

    # 输入enable密码
    tn.write("enable".encode('ascii') + b"\n")
    time.sleep(1)
    tn.write(telnet_decr.encode('ascii') + b"\n")

    # 输入 show run 命令
    commands = [
        'show run'
    ]

    timestr = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    for cmd in commands:
        filename = u'%s_%s_%s.txt' % (ip, cmd.replace(' ', '_'), timestr)
        save = open(filename, 'w')
        print('备份配置启动，正在执行命令：' + cmd)
        tn.write("show run".encode('ascii') + b"\n")

        for i in range(50):
            tn.write(b" ")
            i = i + 1
        time.sleep(5)

        result1 = tn.read_very_eager()  # 获得结果
        save.write(result1.decode('ascii'))
        print('配置备份成功，结果保存于当前目录%s中!' % filename)
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
        print('-' * 50 + '\n')

    # 命令执行完毕后，终止Telnet连接（或输入exit退出）
    tn.close()

def ssh_login(ip):
    cisco_3850 = {
        'device_type': 'cisco_ios',
        'ip': ip,
        'username': telnet_decr_user,
        'password':  telnet_decr,
        'port': 22,
        'secret': telnet_decr
    }
    print('\n')
    print('-' * 50)
    print('正连接交换机：%s\n' % (ip))
    net_connect = ConnectHandler(**cisco_3850)
    net_connect.enable()
    commands = [
        'show run'
    ]

    timestr = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    for cmd in commands:
        filename = u'%s_%s_%s.txt' % (ip, cmd.replace(' ', '_'), timestr)
        save = open(filename, 'w')
        print('正在执行命令：' + cmd)
        result = net_connect.send_command(cmd)
        save.write(result)
        print('配置备份成功，结果保存于当前目录%s中!' % filename)
        print('-' * 50 + '\n')
    net_connect.disconnect()

if __name__ == '__main__':
    telnet = [
        '12.1.1.1',
        '12.1.1.2',
        '12.1.1.3'
    ]

    ssh = [
        '192.168.139.18'
    ]

    for ip in telnet:
        telnet_login(ip)

    # for ip in ssh:
    #     ssh_login(ip)
