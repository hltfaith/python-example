# coding=utf-8
##  author: Changhao
##  Mail: wu_chang_hao@qq.com
##  Date: 2019-06-07
##  Version: vd.1.0
#

'''
读取文件字符, 检查是否会解码失败!
'''

with open('aa.log', 'r', encoding='utf-8') as f:
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
f.close()



