import optparse
import socket
import json

class FtpClient(object):
    """ftp客户端"""
    MSG_SIZE = 1024  # 消息最长1024

    def __init__(self):
        self.username = None
        parser = optparse.OptionParser()
        parser.add_option("-s","--server", dest="server", help="ftp server ip_addr")
        parser.add_option("-P","--port",type="int", dest="port", help="ftp server port")
        parser.add_option("-u","--username", dest="username", help="username info")
        parser.add_option("-p","--password", dest="password", help="password info")
        self.options , self.args = parser.parse_args()

        #print(self.options,self.args,type(self.options),self.options.server)
        self.argv_verification()

        self.make_connection()


    def argv_verification(self):
        """检查参数合法性"""
        if not self.options.server or not self.options.port:
            exit("Error: must supply server and port parameters")


    def make_connection(self):
        """建立socket链接"""
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.connect((self.options.server,self.options.port))

    def get_response(self):
        """获取服务器端返回"""
        data = self.sock.recv(self.MSG_SIZE)
        return json.loads(data.decode())


    def auth(self):
        """用户认证"""
        count = 0
        while count < 3:
            username = input("username:").strip()
            if not username:continue
            password = input("password:").strip()

            cmd = {
                'action_type':'auth',
                'username':username,
                'password':password,
            }

            self.sock.send(json.dumps(cmd).encode("utf-8"))
            response = self.get_response()
            print("response:",response)
            if response.get('status_code') == 200:#pass auth
                self.username = username
                return True
            else:
                print(response.get("status_msg"))
            count += 1


    def interactive(self):
        """处理与Ftpserver的所有交互"""
        if self.auth():
            while True:
                user_input  = input("[%s]>>:" % self.username).strip()
                if not user_input:continue

                cmd_list = user_input.split()
                if hasattr(self,"_%s"%cmd_list[0]):
                    func = getattr(self,"_%s"%cmd_list[0])
                    func(cmd_list[1:])
                    #get fil1 --md5


    def parameter_check(self,args,min_args=None,max_args=None,exact_args=None):
        """参数个数合法性检查"""
        if min_args:
            if len(args) < min_args:
                print("must provide at least %s parameters but %s received." %(min_args,len(args)))
                return False
        if max_args:
            if len(args) > max_args:
                print("need at most %s parameters but %s received." %(max_args,len(args)))
                return False

        if exact_args:
            if len(args) != exact_args:
                print("need exactly %s parameters but %s received." % (exact_args, len(args)))
                return False

        return True

    def send_msg(self,action_type,**kwargs ):
        """打包消息并发送到远程"""
        msg_data = {
            'action_type': action_type,
            'fill':''
        }
        msg_data.update(kwargs)

        bytes_msg = json.dumps(msg_data).encode()
        if self.MSG_SIZE > len(bytes_msg):
            msg_data['fill'] = msg_data['fill'].zfill( self.MSG_SIZE - len(bytes_msg))
            bytes_msg = json.dumps(msg_data).encode()

        self.sock.send(bytes_msg)

    def _get(self,cmd_args):
        """download file from ftp server
        1.拿到文件名
        2.发送到远程
        3.等待服务器返回消息
            3.1 如果文件存在， 拿到文件大小
                3.1.1 循环接收
            3.2 文件如果不存在
                print status_msg

        """
        if self.parameter_check(cmd_args,min_args=1):
            filename = cmd_args[0]
            self.send_msg(action_type='get',filename=filename)
            response = self.get_response()
            if response.get('status_code') == 301:# file exist ,ready to receive
                file_size = response.get('file_size')
                received_size = 0
                f = open(filename,"wb")
                while received_size < file_size:
                    if file_size - received_size < 8192:#last recv
                        data = self.sock.recv(  file_size - received_size )
                    else:
                        data = self.sock.recv(8192)
                    received_size += len(data)
                    f.write(data)
                    print(received_size,file_size)
                else:
                    print("---file [%s] recv done,received size [%s]----"%( filename,file_size))
                    f.close()

            else:
                print(response.get('status_msg'))

    def _put(self):
        pass



if __name__ == "__main__":
    client = FtpClient()
    client.interactive() #交互