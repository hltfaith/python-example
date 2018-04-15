import hashlib
import sys, os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
user_home = BASE_DIR + "/db/user_home/"
sys.path.append(BASE_DIR)

def user_encrypt(passwd):

    encr = hashlib.md5()
    encr.update(passwd.encode('utf-8'))
    return encr.hexdigest()

class user_data(object):

    def __init__(self, username, filename, data, file_len):
        self.username = username
        self.filename = filename
        self.data = data
        self.file_len = file_len

    def download(self):
        user_file = user_home + self.username + '/' + self.filename

        user_data = ''
        if os.path.exists(user_file):
            with open(user_file, 'r+') as f:
                user_data = f.read()
                f.close()
            data_len = str(len(user_data))
            tag = self.username + ' ' + self.filename + ' ' + user_data + ' ' + data_len
            return tag

        else:
            tag = 'Nofile' + ' ' + '1' + ' ' + '1' + ' ' + '1'
            return tag

    def show_list(self):
        user_dir = user_home + self.username
        if os.path.exists(user_dir):
            file_list = os.listdir(user_home + self.username)
            aa = ','.join(file_list)
            list_file = aa.replace(",", "\n")
            return str(list_file)

        else:
            os.mkdir(user_dir, 0o777)
            return '该目录没有文件!'

    def upload(self):
        user_dir = user_home + self.username + '/' + self.filename

        if os.path.exists(user_home + self.username):
            with open(user_dir, 'w+') as f:
                f.write(self.data)
                f.close()

        else:
            os.mkdir(user_home + self.username, 0o777)
            with open(user_dir, 'w+') as f:
                f.write(self.data)
                f.close()

        data_len = ''
        with open(user_dir, 'r+') as f:
            data_len = f.read()
            f.close()

        if self.file_len == str(len(data_len)):
            return '文件上传成功'

        else:
            return '文件上传失败!'
