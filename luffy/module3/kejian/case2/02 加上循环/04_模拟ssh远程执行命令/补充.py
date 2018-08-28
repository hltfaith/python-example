#windows
#dir:查看某一个文件夹下的子文件名与子文件夹名
#ipconfig：查看本地网卡的ip信息
#tasklist：查看运行的进程


#linux：
#ls
#ifconfig
#ps aux



#执行系统命令,并且拿到命令的结果
# import os
# res=os.system('xxxxlxxxs /')
# print('命令的结果是：',res)

import subprocess
obj=subprocess.Popen('xxxxxxls /',shell=True,
                 stdout=subprocess.PIPE,
                 stderr=subprocess.PIPE)


print(obj)
print('stdout 1--->: ',obj.stdout.read().decode('utf-8'))
# print('stdout 2--->: ',obj.stdout.read().decode('utf-8'))

print('stderr 1--->: ',obj.stderr.read().decode('utf-8'))
