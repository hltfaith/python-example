# -*- coding: utf-8 -*-
import wx
import wx.xrc
import os, sys

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)

from conn_eolinker import api_interface
from system_check import sys_check

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

        self.rjzx_button5 = wx.Button(self, wx.ID_ANY, u"2. 软件中心", wx.DefaultPosition, wx.DefaultSize, 0)
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

        self.wlzt_label = wx.StaticText(self, wx.ID_ANY, u"网络状态", wx.DefaultPosition, wx.DefaultSize, 0)
        self.wlzt_label.Wrap(-1)
        gSizer2.Add(self.wlzt_label, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        net_status = str(systemcheck.network_check())       # 实例化 网络检查方法

        self.wlzt_value = wx.StaticText(self, wx.ID_ANY, u'{0}'.format(str(net_status)), wx.DefaultPosition, wx.DefaultSize, 0)  # 网络状态显示
        self.wlzt_value.Wrap(-1)
        gSizer2.Add(self.wlzt_value, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.yxxt_label = wx.StaticText(self, wx.ID_ANY, u"影像系统", wx.DefaultPosition, wx.DefaultSize, 0)
        self.yxxt_label.Wrap(-1)
        gSizer2.Add(self.yxxt_label, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.yxxt_value = wx.StaticText(self, wx.ID_ANY, "yingxiangxitong", wx.DefaultPosition, wx.DefaultSize, 0)
        self.yxxt_value.Wrap(-1)
        gSizer2.Add(self.yxxt_value, 0, wx.ALL, 5)

        self.zt_label = wx.StaticText(self, wx.ID_ANY, u"字体", wx.DefaultPosition, wx.DefaultSize, 0)
        self.zt_label.Wrap(-1)
        gSizer2.Add(self.zt_label, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.zt_value = wx.StaticText(self, wx.ID_ANY, "ziti", wx.DefaultPosition, wx.DefaultSize, 0)
        self.zt_value.Wrap(-1)
        gSizer2.Add(self.zt_value, 0, wx.ALL, 5)

        self.dngj_label = wx.StaticText(self, wx.ID_ANY, u"电脑管家", wx.DefaultPosition, wx.DefaultSize, 0)
        self.dngj_label.Wrap(-1)
        gSizer2.Add(self.dngj_label, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.dngj_value = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.dngj_value.Wrap(-1)
        gSizer2.Add(self.dngj_value, 0, wx.ALL, 5)

        self.office_label = wx.StaticText(self, wx.ID_ANY, u"office", wx.DefaultPosition, wx.DefaultSize, 0)
        self.office_label.Wrap(-1)
        gSizer2.Add(self.office_label, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.office_value = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.office_value.Wrap(-1)
        gSizer2.Add(self.office_value, 0, wx.ALL, 5)

        self.ukey_label = wx.StaticText(self, wx.ID_ANY, u"ukey", wx.DefaultPosition, wx.DefaultSize, 0)
        self.ukey_label.Wrap(-1)
        gSizer2.Add(self.ukey_label, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.ukey_value = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.ukey_value.Wrap(-1)
        gSizer2.Add(self.ukey_value, 0, wx.ALL, 5)

        self.SetSizer(gSizer2)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


###########################################################################
## Class rjzx_windows
###########################################################################

class rjzx_windows(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"软件中心", pos=wx.DefaultPosition, size=wx.Size(500, 300),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        self.bqcwxtrjgxwz = wx.StaticText(self, wx.ID_ANY, u"北汽财务系统软件共享网址", wx.DefaultPosition, wx.DefaultSize, 0)
        self.bqcwxtrjgxwz.Wrap(-1)
        self.bqcwxtrjgxwz.SetFont(wx.Font(18, 70, 90, 92, False, "宋体"))

        bSizer7.Add(self.bqcwxtrjgxwz, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 45)

        self.wangzhi = wx.StaticText(self, wx.ID_ANY, u"https://share.weiyun.com/5kjgDWa", wx.DefaultPosition,
                                     wx.DefaultSize, 0)
        self.wangzhi.Wrap(-1)
        self.wangzhi.SetFont(wx.Font(14, 70, 90, 90, False, "宋体"))

        bSizer7.Add(self.wangzhi, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(bSizer7)
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
