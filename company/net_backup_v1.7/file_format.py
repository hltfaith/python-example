import os
import time
import re

current_dir = os.getcwd() + "\\" + time.strftime('%Y-%m-%d')
def rename():
    print('开始转换........')
    start_time = time.localtime()
    all_files = os.listdir(current_dir)
    for i in all_files:
        if re.findall('\.cfg', i):
            with open(current_dir+"\\"+i, 'r') as f:
                read_line = f.read()
                read_line = read_line.replace(' --More--         ', '')

            with open(current_dir+"\\"+i+'.txt', 'w') as fpw:
                fpw.write(read_line)

            os.remove(current_dir+"\\"+i)
    print('转换成功！！！ 请按3退出......')
