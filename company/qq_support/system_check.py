
import os, sys
import re
import subprocess


class sys_check(object):

    # 网络检测
    def network_check(self):
        cmd = subprocess.Popen('ping -n 1 finance.baicfc.com', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        out = cmd.stdout.read()
        regex = re.compile('0% 丢失')
        out = bytes.decode(out, encoding='gbk')
        if regex.findall(out):
            return '连接正常'

        else:
            return '连接失败'

    # 影像系统检测
    def yx_system_check(self):
        cmd = subprocess.Popen('tasklist | findstr LiveServer.exe', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        out = cmd.stdout.read()
        out = bytes.decode(out, encoding='gbk')
        if len(out) == 0:

            if os.path.isfile('D:\\Sinosoft\\EasyScan 5.0\\LiveServer.exe'):
                return '程序未启动'

            else:
                return '程序未安装'

        else:

            cmd_server = subprocess.Popen('net start | findstr DefaultInstance', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            cmd_server_out = cmd_server.stdout.read()
            cmd_server_out = bytes.decode(cmd_server_out, encoding='gbk')

            if len(cmd_server_out) == 0:
                return '服务未启动'

            else:
                return '启动正常'

    # 字体检测
    def ziti_check(self):
        if os.path.isfile('C:\\Windows\\Fonts\\ADVC128B.TTF') and os.path.isfile('C:\\Windows\\Fonts\\ADVC128C.TTF') and os.path.isfile('C:\\Windows\\Fonts\\code128.ttf') and os.path.isfile('C:\\Windows\\Fonts\\STZHONGS.TTF'):
            return '安装正常'
        else:
            return '未安装'

    # 电脑管家检测
    def dngj_check(self):
        cmd = subprocess.Popen('tasklist | findstr QQPCTray.exe', stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE, shell=True)
        out = cmd.stdout.read()
        out = bytes.decode(out, encoding='gbk')

        if len(out) == 0:
            return '正常状态'
        else:
            return '请卸载程序'

    # WPS软件检测
    def office_check(self):
        cmd = subprocess.Popen('tasklist | findstr wps.exe', stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, shell=True)
        out = cmd.stdout.read()
        out = bytes.decode(out, encoding='gbk')

        if len(out) == 0:
            return '正常状态'
        else:
            return '请卸载程序'

    # ukey驱动检测
    def ukey_check(self):
        if os.path.isfile('C:\\Program Files (x86)\\EnterSafe\ePass3000GM\\certd3kGM.exe') or os.path.isfile('C:\\Program Files (x86)\\ngsrv\\epsng_certd.exe'):
            return '已安装'

        else:
            return '未安装'
