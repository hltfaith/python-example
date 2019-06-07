# coding=utf-8
##  author: Changhao
##  Mail: changhao.wu@cs2c.com.cn
##  Date: 2019-06-06
##  Version: vd.1.0
#

import datetime
import time
import re
import os

def auditFormat(audit_dir, outfile):

    '''
    将多个 audit 日志合并成一个log日志文件, 并将时间戳转换成 2019-06-06 格式
    :return:
    '''

    print('audit,blaudit logFile merge format - start')

    auditfileList = []                  # audit 日志文件列表
    blauditfileList = []                # blaudit 日志文件列表

    # 遍历audit目录文件名
    for i in os.listdir(audit_dir):
        auditfileName = re.findall('^audit.*log.*', i)
        blauditfileName = re.findall('bl+.*', i)

        if len(auditfileName) != 0:
            auditfileList.append(auditfileName[0])
        if len(blauditfileName) != 0:
            blauditfileList.append(blauditfileName[0])

    def appendAudit():

        # 生成新 audit 日志文件
        fileNew = open(outfile+r'\audit.outfile.log', 'w+', encoding='utf-8')

        for filename in auditfileList:
            with open(audit_dir+'\\'+filename, 'r', encoding='utf-8') as f:
                for i in f.readlines():
                    a1 = re.search('\d.*\d\.', i).group()
                    a2 = re.search('\d+', a1).group()           # 匹配 时间戳
                    a3 = re.search('\d.*\d\)', i).group()       # 匹配()内容
                    a4 = re.search('\d.*\d', a3).group()        # 匹配()内容

                    # 时间戳转换
                    time_local = time.localtime(int(a2))
                    date = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
                    # 替换时间戳
                    fileNew.write(i.replace(a4, date))

            f.close()
        fileNew.close()

    def appendBLaudit():

        # 生成新 blaudit 日志文件
        fileNew = open(outfile + r'\blaudit.outfile.log', 'w+', encoding='utf-8')

        for filename in blauditfileList:
            with open(audit_dir + '\\' + filename, 'r', encoding='utf-8') as f:
                for i in f.readlines():
                    a3 = re.search('\d+\d\.', i).group()  # 匹配()内容
                    a4 = re.search('\d.*\d', a3).group()  # 匹配()内容

                    # 时间戳转换
                    time_local = time.localtime(int(a4))
                    date = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
                    # 替换时间戳
                    fileNew.write(i.replace(a4, date))

            f.close()
        fileNew.close()

    appendAudit()
    appendBLaudit()

    print('audit,blaudit logFile merge format - end')

def messagesFormat(messages_dir):

    '''
    messages 日志统计记录出, 日志日期
    :param messages_dir:
    :return: 返回
    '''

    print('messages count log dateName -- start')

    # 遍历messages目录文件名
    messagesfileList = []
    for i in os.listdir(messages_dir):
        messagesfileName = re.findall('^messages.*', i)

        if len(messagesfileName) != 0:
            messagesfileList.append(messagesfileName[0])

    # 统计同一天日期  格式: May 29
    dateName = []
    for filename in messagesfileList:
        with open(messages_dir + '\\' + filename, 'r', encoding='utf-8') as f:

            while True:
                line = f.readline()
                if not line:
                    break
                else:
                    try:
                        aa = line.split()
                        if not len(aa) <= 1:
                            if re.search('^\w{3}$', str(aa[0])):
                                if re.search('^\d{2}$', str(aa[1])):
                                    bb = str(aa[0] + ' ' + aa[1])
                                    dateName.append(bb)

                    except UnicodeEncodeError:
                        pass
                    except AttributeError:
                        pass

                '''  检测字符解码是否错误
                i = 0
                while True:
                    i += 1
                    print(i)
                    line = f.readline()
                    if not line:
                        break
                    else:
                        try:
                            # print(line)
                            #             print(line.decode('utf8'))
                            # line.decode('utf8')
                            line.decode('utf-8')
                            # 为了暴露出错误，最好此处不print
                        except:
                            print(str(line))
                '''

        f.close()

    print('messages count log dateName -- end')
    print('Program run messages count load ....  ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    return set(dateName)

class COUNTSIZE(object):

    '''
    日志大小统计, 按每天为单位计算
    '''

    def __init__(self):
        self.sourceFile = r'D:\share\log-北信源'
        self.outfile = r'D:\share\log-北信源'

    def matchdate(self, name):

        '''
        匹配时间
        :return:
        '''

        with open(self.sourceFile + r'\%s.outfile.log' % name, 'r', encoding='utf-8') as f:
            dateList = []               # 日志所产生的天数
            for i in f.readlines():
                dateName = re.findall('\d+-\d+-\d+', i)
                dateList.append(dateName[0])

        f.close()

        return set(dateList)

    def writedir(self, name):

        '''
        将同一天日志存放单独文件, 查看当天日志大小
        :return:
        '''

        print('audit,blaudit write file - start')

        dateMatch = self.matchdate(name)
        for i in dateMatch:
            # 生成新日志文件  [audit.log-2019-06-06]
            fileNew = open(self.outfile + r'\%s-day.log-' % name + str(i), 'w+', encoding='utf-8')

            with open(self.sourceFile + r'\%s.outfile.log' % name, 'r', encoding='utf-8') as f:
                for k in f.readlines():
                    if str(i) == re.findall('\d+-\d+-\d+', k)[0]:
                        fileNew.write(k)
                f.close()
            fileNew.close()

        print('audit,blaudit write file - end')

    def msgwrite(self, messages_dir, name):

        '''
        将 messages 同一天日志写入单独文件
        :return:
        '''

        print('messages log write File - start')
        dateName = messagesFormat(messages_dir)

        for i in dateName:

            print('%s logfile write load......' % str(i))
            # 生成新日志文件  [messages.log-2019-06-06]
            fileNew = open(self.outfile + r'\%s-day.log-' % name + str(i), 'w+', encoding='utf-8')

            with open(self.sourceFile + r'\%s' % name, 'r', encoding='utf-8') as f:
                while True:
                    line = f.readline()
                    if not line:
                        break
                    else:
                        try:
                            aa = line.split()
                            if not len(aa) <= 1:
                                if re.search('^\w{3}$', str(aa[0])):
                                    if re.search('^\d{2}$', str(aa[1])):

                                        char = str(aa[0] + ' ' + aa[1])
                                        if str(i) == char:
                                            fileNew.write(line)

                        except UnicodeEncodeError:
                            pass
                        except AttributeError:
                            pass
                f.close()
            fileNew.close()
            print('%s logfile write success!!' % str(i))
            print('Program run messages write load ....  ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


        print('messages log write File - end')

    def filesize(self):

        print('all logFile Count size - start')

        # 字节bytes转化kb\m\g
        def formatSize(bytes):
            try:
                bytes = float(bytes)
                kb = bytes / 1024
            except:
                print("传入的字节格式不对")
                return "Error"

            if kb >= 1024:
                M = kb / 1024
                if M >= 1024:
                    G = M / 1024
                    return "%.2fG" % (G)
                else:
                    return "%.2fM" % (M)
            else:
                return "%.2fkb" % (kb)

        # 获取文件大小
        def getDocSize(path):
            try:
                size = os.path.getsize(path)
                return formatSize(size)
            except Exception as err:
                print(err)

        for i in os.listdir(self.outfile):
            if re.findall('\d$', i):
                print(i, '  ', getDocSize(self.outfile + '\%s' % i))

        print('all logFile Count size - end')

    def rmfile(self):

        for i in os.listdir(self.outfile):
            if re.findall('\d$', i):
                os.remove(self.outfile + '\\' + i)
            if re.findall('.*outfile.*', i):
                os.remove(self.outfile + '\\' + i)

        print('all temp rmfile success!!!')

if __name__ == '__main__':

    '''
    使用声明
    注意：将要统计的日志另存放在单独一个空目录中， 避免不必要的冲突!!!
    '''

    start = datetime.datetime.now()
    print('程序运行开始 ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    # 定义 audit 日志目录, 定义 messages 日志目录,  以及outfile缓存区目录
    audit_dir = r'D:\share\log-北信源\var-log\audit'
    messages_dir = r'D:\share\log-北信源'
    outfile = r'D:\share\log-北信源'

    # Audit,blaudit 日志时间戳初始转换 2019-06-06 格式
    auditFormat(audit_dir, outfile)

    # 以天为单位, log分段写入单独文件
    run = COUNTSIZE()
    run.writedir('audit')
    run.writedir('blaudit')
    run.msgwrite(messages_dir, 'messages')

    # 统计日志大小
    run.filesize()

    # 删除缓存区目录文件
    run.rmfile()

    print('程序运行结束 ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    end = datetime.datetime.now()
    m, s = divmod(int((end - start).seconds), 60)
    h, m = divmod(m, 60)
    print('共消耗时长：' + ("%02d:%02d:%02d" % (h, m, s)))

