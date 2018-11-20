
import paramiko

#SSHClient 封装 Transport

transport = paramiko.Transport(('10.111.111.81', 22))
transport.connect(username='root', password='123456')

ssh = paramiko.SSHClient()
ssh._transport = transport

stdin, stdout, stderr = ssh.exec_command('df')
print(stdout.read())

transport.close()


