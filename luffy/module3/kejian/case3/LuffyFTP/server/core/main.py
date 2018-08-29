import socket
from conf import settings
import json,hashlib,os
import configparser

class FTPServer(object):
    """处理与客户端所有的交互的socket server"""

    STATUS_CODE ={
        200 : "Passed authentication!",
        201 : "Wrong username or password!",
        300 : "File does not exist !",
        301 : "File exist , and this msg include the file size- !",
    }

    MSG_SIZE = 1024 #消息最长1024

    def __init__(self,management_instance):
        self.management_instance = management_instance
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.bind((settings.HOST,settings.PORT))
        self.sock.listen(settings.MAX_SOCKET_LISTEN)
        self.accounts = self.load_accounts()
        self.user_obj = None


    def run_forever(self):
        """启动socket server"""
        print('starting LuffyFtp server on %s:%s'.center(50,'-') %(settings.HOST,settings.PORT))

        while True:
            self.request,self.addr = self.sock.accept()
            print("got a new connection from %s....." %(self.addr,))
            self.handle()

    def handle(self):
        """处理与用户的所有指令交互"""
        while True:

            raw_data = self.request.recv(self.MSG_SIZE)
            print('------->',raw_data)
            if not raw_data:
                print("connection %s is lost ...." % (self.addr,))
                del self.request,self.addr
                break

            data = json.loads(raw_data.decode("utf-8"))
            action_type = data.get('action_type') #None
            if action_type:
                if hasattr(self,"_%s" % action_type):
                    func = getattr(self,"_%s" % action_type)
                    func(data)

            else:
                print("invalid command,")


    def load_accounts(self):
        """加载所有账号信息"""
        config_obj = configparser.ConfigParser()
        config_obj.read(settings.ACCOUNT_FILE)

        print(config_obj.sections())
        return config_obj


    def authenticate(self,username,password):
        """用户认证方法"""
        if username in self.accounts:
            _password = self.accounts[username]['password']
            md5_obj = hashlib.md5()
            md5_obj.update(password.encode())
            md5_password = md5_obj.hexdigest()
            print("passwd:",_password,md5_password)
            if md5_password == _password:
                #print("passed authentication...")
                #set user obj
                self.user_obj = self.accounts[username]
                #self.current_user_home= os.path.join(settings.USER_HOME_DIR,username)
                self.user_obj['home']= os.path.join(settings.USER_HOME_DIR,username) #/home/alex
                #set user home directory

                return True
            else:
                #print("wrong username or password ")
                return  False
        else:
            #print("wrong username or password 2")
            return False

    def send_response(self,status_code,*args,**kwargs):
        """
        打包发送消息给客户端
        :param status_code:
        :param args:
        :param kwargs: {filename:ddd,filesize:222}
        :return:
        """
        data = kwargs
        data['status_code'] = status_code
        data['status_msg'] = self.STATUS_CODE[status_code]
        data['fill'] = ''

        bytes_data = json.dumps(data).encode()

        if len(bytes_data) < self.MSG_SIZE:
            data['fill'] = data['fill'].zfill(  self.MSG_SIZE - len(bytes_data))
            bytes_data = json.dumps(data).encode()

        self.request.send(bytes_data)

    def _auth(self,data):
        """处理用户认证请求"""
        print("auth ",data )
        if self.authenticate(data.get('username'),data.get('password')):
            print('pass auth....')

            #1. 消息内容，状态码
            #2. json.dumps
            #3 . encode
            self.send_response(status_code=200)

        else:
            self.send_response(status_code=201)


    def _get(self,data):
        """client downloads file through this method
            1. 拿到文件名
            2. 判断文件是否存在
                2.1 如果存在， 返回状态码+文件大小
                    2.1.1打开文件，发送文件内容
                2.2 如果不存在， 返回状态码
            3.
        """
        filename = data.get('filename')
        full_path = os.path.join(self.user_obj['home'],filename)
        if os.path.isfile(full_path):
            filesize = os.stat(full_path).st_size
            self.send_response(301,file_size=filesize)
            print("ready to send file ")
            f = open(full_path,'rb')
            for line in f:
                self.request.send(line)
            else:
                print('file send done..',full_path)
            f.close()


        else:
            self.send_response(300)
