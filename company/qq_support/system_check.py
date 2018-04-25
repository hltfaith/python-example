
import os, sys
import re
import subprocess


class sys_check(object):

    def network_check(self):
        cmd = subprocess.Popen('ping -n 1 finance.baicfc.com', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        out = cmd.stdout.read()
        regex = re.compile('0% 丢失')
        out = bytes.decode(out, encoding='gbk')
        if regex.findall(out):
            return '连接正常'

        else:
            return '连接失败'


    def yx_system_check(self):
        pass

    def ziti_check(self):
        pass

    def dngj_check(self):
        pass

    def office_check(self):
        pass

    def ukey_check(self):
        pass



# aa = sys_check()
# a1 = str(aa.network_check())
# print(type(a1))
