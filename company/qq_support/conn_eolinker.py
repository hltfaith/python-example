from urllib import request

def api_interface():

    #api = 'http://result.eolinker.com/uuzXvTFb148a117768a7c0cfa61c8b016c26066af3e0a47?uri=/test/v1'   #测试
    api = 'http://result.eolinker.com/uuzXvTFb148a117768a7c0cfa61c8b016c26066af3e0a47?uri=/shengchan/v1.5'   #生产
    response = request.urlopen(api)
    html = response.read()
    html = html.decode('utf-8')
    data = eval(html)

    #api = '''{ 1: {'提示：影像系统启动失败 报错':['1. 检查客户端是否安装','2. 桌面右下角是否有一个服务启动的标志','3. 使用IE浏览器或360浏览器']}, 2: {'提示：MS Office is not installed 报错':['1. 检查下是否安装office 办公软件','2. 如果安装WPS办公软件请卸载掉','3. 关闭电脑管家软件','4. 近期改动过IE浏览器吗','5. 使用IE浏览器或360浏览器']}, 3: {'提示：The useris allready connected to the Server with same machine. Please try later. 报错': ['1. 登录后没有正确退出导致 (强制关闭网页导致)','2. 解决方法：使用不同网络登录，然后正确退出。']}, 4: {'提示：请确认uKey是否插入 报错': ['1. 检查uKey驱动是否安装', '2. 近期改动过IE浏览器吗', '3. 未安装uKey驱动请索要，备注(ukey有北汽财务字样为新版ukey, ukey蓝色外观为旧版ukey)']}, 5: {'兼容性问题': ['1. 比如下拉框莫名灰色状态，无法点击输入','2. 比如选择不了车型，打开为灰色','3. 解决方法：运行脚本(1-EasyScan浏览器自动配置-IE8-IE11.cmd) --> 重启IE浏览器 --> IE浏览器或360浏览器测试','注：运行脚本找机器人索要']}, 6: {'浏览器推荐': ['1. IE浏览器','(1) 初始化配置 ---> 运行下这个脚本(1-EasyScan浏览器自动配置-IE8-IE11.cmd)','2. 360安全浏览器','(1)同上']}, 7: {'test': ['1. test', '2. test2']} }'''
    #data = eval(api)

    return data
