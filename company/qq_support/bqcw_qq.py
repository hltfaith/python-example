# -*- coding: utf-8 -*-
import wx
import wx.xrc
import os, sys

# BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASEDIR)

from conn_eolinker import api_interface
from system_check import sys_check
from auto_install import soft_install


###########################################################################
## Class bqcw
###########################################################################

class bqcw(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"北汽财务系统故障助手v1", pos=wx.DefaultPosition,
                          size=wx.Size(299, 303), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetExtraStyle(wx.FRAME_EX_CONTEXTHELP)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.cjgz_button4 = wx.Button(self, wx.ID_ANY, u"1. 常见故障", wx.Point(-1, -1), wx.Size(-1, -1), 0)
        self.cjgz_button4.SetFont(wx.Font(15, 70, 90, 90, False, "宋体"))

        bSizer2.Add(self.cjgz_button4, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 25)

        self.rjzx_button5 = wx.Button(self, wx.ID_ANY, u"2. 软件安装", wx.DefaultPosition, wx.DefaultSize, 0)
        self.rjzx_button5.SetFont(wx.Font(15, 70, 90, 90, False, "宋体"))

        bSizer2.Add(self.rjzx_button5, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 25)

        self.xtjc_button6 = wx.Button(self, wx.ID_ANY, u"3. 系统检测", wx.DefaultPosition, wx.DefaultSize, 0)
        self.xtjc_button6.SetFont(wx.Font(15, 70, 90, 90, False, "宋体"))

        bSizer2.Add(self.xtjc_button6, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 25)

        self.SetSizer(bSizer2)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_ACTIVATE, self.cjgz)
        self.cjgz_button4.Bind(wx.EVT_BUTTON, self.cjgz_button)
        self.rjzx_button5.Bind(wx.EVT_BUTTON, self.rjzx_button)
        self.xtjc_button6.Bind(wx.EVT_BUTTON, self.xtjc_button)


    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def cjgz(self, event):
        event.Skip()

    def cjgz_button(self, event):
        app = wx.App(False)
        frame = cjgz(None)
        frame.Show(True)
        # start the applications
        app.MainLoop()
        event.Skip()

    def rjzx_button(self, event):
        app = wx.App(False)
        frame = rjzx_windows(None)
        frame.Show(True)
        # start the applications
        app.MainLoop()
        event.Skip()

    def xtjc_button(self, event):
        app = wx.App(False)
        frame = xtjc_windows(None)
        frame.Show(True)
        # start the applications
        app.MainLoop()
        event.Skip()



###########################################################################
## Class cjgz
###########################################################################

data = api_interface()

class cjgz(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"常见故障", pos=wx.DefaultPosition, size=wx.Size(565, 348),
                           style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        panel = wx.Panel(self)
        box = wx.BoxSizer(wx.VERTICAL)

        list_data = []

        for i in data:
            for k in data[i]:
                list_data.append(k)

        self.choice = wx.Choice(panel, choices=list_data)
        box.Add(self.choice, 0, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        #self.ff_label = wx.StaticText(panel, label="请选择故障问题类型", style=wx.ALIGN_CENTRE)
        self.ff_label = wx.StaticText(panel, label="请选择故障问题类型", style=wx.ALIGN_LEFT)
        box.Add(self.ff_label, 0, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 20)

        box.AddStretchSpacer()
        self.choice.Bind(wx.EVT_CHOICE, self.OnChoice)
        panel.SetSizer(box)
        self.Centre()
        self.Show()

        self.Bind(wx.EVT_ACTIVATE, self.cjgz_windows)
        self.choice.Bind(wx.EVT_CHOICE, self.OnChoice)

    def __del__(self):
        pass

    def cjgz_windows(self, event):
        event.Skip()

    def OnChoice(self, event):

        ## 循环 解决方法步骤
        data_str = ''
        for i in data:
            for k in data[i]:
                if self.choice.GetString(self.choice.GetSelection()) == k:
                    for n in data[i][k]:
                        data_str += n + '|'
        value = data_str.replace('|', '\n')
        self.ff_label.SetLabel(value)
        event.Skip()

###########################################################################
## Class xtjc_windows
###########################################################################

class xtjc_windows(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"系统检测", pos=wx.DefaultPosition, size=wx.Size(243, 300),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        gSizer2 = wx.GridSizer(0, 2, 0, 0)

        systemcheck = sys_check()         # 实例化类

        self.wlzt_label = wx.StaticText(self, wx.ID_ANY, u"网络状态：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.wlzt_label.Wrap(-1)
        gSizer2.Add(self.wlzt_label, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        net_status = str(systemcheck.network_check())       # 实例化 网络检查方法

        self.wlzt_value = wx.StaticText(self, wx.ID_ANY, u'{0}'.format(str(net_status)), wx.DefaultPosition, wx.DefaultSize, 0)  # 网络状态显示
        self.wlzt_value.Wrap(-1)
        gSizer2.Add(self.wlzt_value, 0, wx.ALL , 5)

        self.yxxt_label = wx.StaticText(self, wx.ID_ANY, u"影像系统：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.yxxt_label.Wrap(-1)
        gSizer2.Add(self.yxxt_label, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL , 5)

        yx_system_status = str(systemcheck.yx_system_check())  # 实例化 影像系统检查方法

        self.yxxt_value = wx.StaticText(self, wx.ID_ANY, "{0}".format(str(yx_system_status)), wx.DefaultPosition, wx.DefaultSize, 0)
        self.yxxt_value.Wrap(-1)
        gSizer2.Add(self.yxxt_value, 0, wx.ALL, 5)

        self.zt_label = wx.StaticText(self, wx.ID_ANY, u"字      体：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.zt_label.Wrap(-1)
        gSizer2.Add(self.zt_label, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL , 5)

        ziti_status = str(systemcheck.ziti_check())  # 实例化 字体检查方法

        self.zt_value = wx.StaticText(self, wx.ID_ANY, "{0}".format(str(ziti_status)), wx.DefaultPosition, wx.DefaultSize, 0)
        self.zt_value.Wrap(-1)
        gSizer2.Add(self.zt_value, 0, wx.ALL , 5)

        self.dngj_label = wx.StaticText(self, wx.ID_ANY, u"电脑管家：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.dngj_label.Wrap(-1)
        gSizer2.Add(self.dngj_label, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        dngj_status = str(systemcheck.dngj_check())  # 实例化 电脑管家检查方法

        self.dngj_value = wx.StaticText(self, wx.ID_ANY, "{0}".format(str(dngj_status)), wx.DefaultPosition, wx.DefaultSize, 0)
        self.dngj_value.Wrap(-1)
        gSizer2.Add(self.dngj_value, 0, wx.ALL, 5)

        self.office_label = wx.StaticText(self, wx.ID_ANY, u"WPS软件：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.office_label.Wrap(-1)
        gSizer2.Add(self.office_label, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        offices_status = str(systemcheck.office_check())  # 实例化 WPS检查方法

        self.office_value = wx.StaticText(self, wx.ID_ANY, "{0}".format(str(offices_status)), wx.DefaultPosition, wx.DefaultSize, 0)
        self.office_value.Wrap(-1)
        gSizer2.Add(self.office_value, 0, wx.ALL, 5)

        self.ukey_label = wx.StaticText(self, wx.ID_ANY, u"ukey驱动：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.ukey_label.Wrap(-1)
        gSizer2.Add(self.ukey_label, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        ukey_status = str(systemcheck.ukey_check())  # 实例化 ukey检查方法

        self.ukey_value = wx.StaticText(self, wx.ID_ANY, "{0}".format(str(ukey_status)), wx.DefaultPosition, wx.DefaultSize, 0)
        self.ukey_value.Wrap(-1)
        gSizer2.Add(self.ukey_value, 0, wx.ALL, 5)

        self.SetSizer(gSizer2)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass

class rjzx_windows(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"软件自动化安装", pos=wx.DefaultPosition, size=wx.Size(312, 440),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        gSizer7 = wx.GridSizer(0, 2, 0, 0)

        self.ie_label = wx.StaticText(self, wx.ID_ANY, u"IE浏览器配置", wx.DefaultPosition, wx.DefaultSize, 0)
        self.ie_label.Wrap(-1)
        gSizer7.Add(self.ie_label, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.le_button = wx.Button(self, wx.ID_ANY, u"安装", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer7.Add(self.le_button, 0, wx.ALL, 5)

        self.yx_label = wx.StaticText(self, wx.ID_ANY, u"影 像 系 统", wx.DefaultPosition, wx.DefaultSize, 0)
        self.yx_label.Wrap(-1)
        gSizer7.Add(self.yx_label, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.yx_button = wx.Button(self, wx.ID_ANY, u"安装", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer7.Add(self.yx_button, 0, wx.ALL, 5)

        self.adobe_label = wx.StaticText(self, wx.ID_ANY, u" adobe reader", wx.DefaultPosition, wx.DefaultSize, 0)
        self.adobe_label.Wrap(-1)
        gSizer7.Add(self.adobe_label, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.adobe_button = wx.Button(self, wx.ID_ANY, u"安装", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer7.Add(self.adobe_button, 0, wx.ALL, 5)

        self.ziti_label = wx.StaticText(self, wx.ID_ANY, u"字       体", wx.DefaultPosition, wx.DefaultSize, 0)
        self.ziti_label.Wrap(-1)
        gSizer7.Add(self.ziti_label, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.ziti_button = wx.Button(self, wx.ID_ANY, u"安装", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer7.Add(self.ziti_button, 0, wx.ALL, 5)

        self.newkey_label = wx.StaticText(self, wx.ID_ANY, u"新  KEY", wx.DefaultPosition, wx.DefaultSize, 0)
        self.newkey_label.Wrap(-1)
        gSizer7.Add(self.newkey_label, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.newkey_button = wx.Button(self, wx.ID_ANY, u"安装", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer7.Add(self.newkey_button, 0, wx.ALL, 5)

        self.oldkey_label = wx.StaticText(self, wx.ID_ANY, u"旧  KEY", wx.DefaultPosition, wx.DefaultSize, 0)
        self.oldkey_label.Wrap(-1)
        gSizer7.Add(self.oldkey_label, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.oldkey_button = wx.Button(self, wx.ID_ANY, u"安装", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer7.Add(self.oldkey_button, 0, wx.ALL, 5)

        self.SetSizer(gSizer7)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.le_button.Bind(wx.EVT_BUTTON, self.ie_install)
        self.yx_button.Bind(wx.EVT_BUTTON, self.yx_install)
        self.adobe_button.Bind(wx.EVT_BUTTON, self.adobe_install)
        self.ziti_button.Bind(wx.EVT_BUTTON, self.ziti_install)
        self.newkey_button.Bind(wx.EVT_BUTTON, self.newkey_install)
        self.oldkey_button.Bind(wx.EVT_BUTTON, self.oldkey_install)

    def __del__(self):
        pass

    def ie_install(self, event):
        auto = soft_install()
        auto.ie_config()
        app = wx.App(False)
        frame = ie_windows(None)
        frame.Show(True)
        app.MainLoop()

    def yx_install(self, event):
        auto = soft_install()
        auto.yxsystem_install()
        app = wx.App(False)
        frame = yx_windows(None)
        frame.Show(True)
        app.MainLoop()

    def adobe_install(self, event):
        auto = soft_install()
        auto.adobe_install()
        app = wx.App(False)
        frame = adobe_windows(None)
        frame.Show(True)
        app.MainLoop()

    def ziti_install(self, event):
        auto = soft_install()
        auto.ziti_install()
        app = wx.App(False)
        frame = ziti_windows(None)
        frame.Show(True)
        app.MainLoop()

    def newkey_install(self, event):
        auto = soft_install()
        auto.newkey_install()
        app = wx.App(False)
        frame = key_windows(None)
        frame.Show(True)
        app.MainLoop()

    def oldkey_install(self, event):
        auto = soft_install()
        auto.oldkey_install()
        app = wx.App(False)
        frame = key_windows(None)
        frame.Show(True)
        app.MainLoop()


###########################################################################
## Class ie_windows
###########################################################################

class ie_windows(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"提示", pos=wx.DefaultPosition, size=wx.Size(297, 141),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText14 = wx.StaticText(self, wx.ID_ANY, u"\n\nIE浏览器配置成功！！！", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText14.Wrap(-1)
        self.m_staticText14.SetFont(wx.Font(12, 70, 90, 92, False, "宋体"))

        bSizer2.Add(self.m_staticText14, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.STAY_ON_TOP, 5)

        self.SetSizer(bSizer2)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


###########################################################################
## Class yx_windows
###########################################################################

class yx_windows(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"提示", pos=wx.DefaultPosition, size=wx.Size(297, 141),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText16 = wx.StaticText(self, wx.ID_ANY, u"\n\n影像系统安装成功！！！", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText16.Wrap(-1)
        self.m_staticText16.SetFont(wx.Font(12, 70, 90, 92, False, "宋体"))

        bSizer3.Add(self.m_staticText16, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.STAY_ON_TOP, 5)

        self.SetSizer(bSizer3)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


###########################################################################
## Class adobe_windows
###########################################################################

class adobe_windows(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"提示", pos=wx.DefaultPosition, size=wx.Size(297, 141),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText17 = wx.StaticText(self, wx.ID_ANY, u"\n\nAdobe Reader 安装成功！！！", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText17.Wrap(-1)
        self.m_staticText17.SetFont(wx.Font(12, 70, 90, 92, False, "宋体"))

        bSizer4.Add(self.m_staticText17, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.STAY_ON_TOP, 5)

        self.SetSizer(bSizer4)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


###########################################################################
## Class key_windows
###########################################################################

class key_windows(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"提示", pos=wx.DefaultPosition, size=wx.Size(297, 141),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText18 = wx.StaticText(self, wx.ID_ANY, u"\n\nUkey 驱动已安装成功！！！", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText18.Wrap(-1)
        self.m_staticText18.SetFont(wx.Font(12, 70, 90, 92, False, "宋体"))

        bSizer5.Add(self.m_staticText18, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.STAY_ON_TOP, 5)

        self.SetSizer(bSizer5)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


class ziti_windows(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"提示", pos=wx.DefaultPosition, size=wx.Size(297, 141),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText19 = wx.StaticText(self, wx.ID_ANY, u"\n\n请将4个字体文件复制到C:\Windows\Fonts目录", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText19.Wrap(-1)
        self.m_staticText19.SetFont(wx.Font(9, 70, 90, 90, False, "宋体"))

        bSizer6.Add(self.m_staticText19, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.STAY_ON_TOP, 5)

        self.SetSizer(bSizer6)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


if __name__ == '__main__':
    app = wx.App(False)
    frame = bqcw(None)
    frame.Show(True)
    # start the applications
    app.MainLoop()
