
import openpyxl
import paramiko


user_data = ''

def data_xlsx(data):

    ws = openpyxl.Workbook()
    ws1 = ws.active
    dest_filename = 'data.xlsx'

    num1 = 1
    list_num = ['1', '2', '3']
    for i in list_num:
        a = ('A' + str(num1))
        ws1[a] = data
        a = i
        num1 += 1

    ws.save(dest_filename)


class oracle_sql():
    def __init__(self, ip, port, username, password):
        pass

    def exec_cmd(self):
        pass


def ssh2(ip, port, username, password, timeout=10):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, 22, username, password)

    stdin, oracle, stderr = ssh.exec_command('cat oracle.txt')
    #pprint.pprint(stdout.read().decode('utf-8').split('\n'))
    stdin, ls_l, stderr = ssh.exec_command('ls -l')
    oracle = oracle.read().decode('utf-8')#.split('\n')
    data_xlsx(oracle)

def menu():
    falg = '''
    *************************************
            oracle Sql 语句数据导出
            
            1. 单服务器数据导出
            
    *************************************
    '''
    while True:
        pass


if __name__ == '__main__':
    ssh2('10.79.1.202', 22, 'root', 'root123')
    #data_xlsx()


