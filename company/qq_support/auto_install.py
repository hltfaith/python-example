import os,sys

#DASE_DIR = os.path.dirname(os.path.abspath(__file__))
DASE_DIR = os.getcwd()
sys.path.append(DASE_DIR)

wget_usg = DASE_DIR + "\\" + 'wget.exe'

class soft_install(object):

    def __init__(self):
        self.yx_api = 'ftp://wuchanghao:xxxxxxx@013.3vftp.com/EasyScanV5.0.0.7(20170724)_v10.exe'
        self.jb_api = 'ftp://wuchanghao:xxxxxxx@013.3vftp.com/1-EasyScan浏览器自动配置-IE8-IE11.cmd'
        self.adobe_api = 'ftp://wuchanghao:xxxxxxx@013.3vftp.com/AdbeRdr940_zh_CN.exe'
        self.zt1_api = 'ftp://wuchanghao:xxxxxxx@013.3vftp.com/ADVC128B_0.TTF'
        self.zt2_api = 'ftp://wuchanghao:xxxxxxx@013.3vftp.com/ADVC128C_0.TTF'
        self.zt3_api = 'ftp://wuchanghao:xxxxxxx@013.3vftp.com/code128.ttf'
        self.zt4_api = 'ftp://wuchanghao:xxxxxxx@013.3vftp.com/STZHONGS.TTF'
        self.oldkey_api = 'ftp://wuchanghao:xxxxxxx@013.3vftp.com/eps3k_stdSimpChinese.exe'
        self.newkey_api = 'ftp://wuchanghao:xxxxxxx@013.3vftp.com/有北汽财务字样的Ukey驱动.exe'

    # IE浏览器配置
    def ie_config(self):
        os.system(wget_usg + ' ' + self.jb_api)                               # 下载脚本
        os.system(DASE_DIR+'\\'+'1-EasyScan浏览器自动配置-IE8-IE11.cmd')       # 自动配置脚本
        os.system('del /F '+'1-EasyScan浏览器自动配置-IE8-IE11.cmd')           # 删除脚本


    # 影像系统安装
    def yxsystem_install(self):
        os.system(wget_usg + ' ' + self.yx_api)
        os.system('start /wait ' + DASE_DIR + '\\' + 'EasyScanV5.0.0.7(20170724)_v10.exe /s')
        os.system('del /F ' + 'EasyScanV5.0.0.7(20170724)_v10.exe')

    # adobe reader安装
    def adobe_install(self):
        os.system(wget_usg + ' ' + self.adobe_api)
        os.system('start /wait ' + DASE_DIR + '\\' + 'AdbeRdr940_zh_CN.exe /sAll /msi /norestart ALLUSERS=1 EULA_ACCEPT=YES')
        os.system('del /F ' + 'AdbeRdr940_zh_CN.exe')

    # 字体安装
    def ziti_install(self):
        os.system(wget_usg + ' ' + self.zt1_api)
        os.system(wget_usg + ' ' + self.zt2_api)
        os.system(wget_usg + ' ' + self.zt3_api)
        os.system(wget_usg + ' ' + self.zt4_api)

    # 新key安装
    def newkey_install(self):
        os.system(wget_usg + ' ' + self.newkey_api)
        os.system('start /wait ' + DASE_DIR + '\\' + '有北汽财务字样的Ukey驱动.exe /S')
        os.system('del /F ' + '有北汽财务字样的Ukey驱动.exe')

    # 旧key安装
    def oldkey_install(self):
        os.system(wget_usg + ' ' + self.oldkey_api)
        os.system('start /wait ' + DASE_DIR + '\\' + 'eps3k_stdSimpChinese.exe /S')
        os.system('del /F ' + 'eps3k_stdSimpChinese.exe')
