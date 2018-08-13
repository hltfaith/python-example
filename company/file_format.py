import os

current_dir = os.path.dirname(__file__)+"/"
def rename():
    filename = '172.16.100.17_show_run_2018-08-13.cfg'
    with open(filename, 'r') as f:
        read_line = f.read()
        read_line = read_line.replace(' --More--         ', '')

    with open(filename+'.txt', 'w') as fpw:
        fpw.write(read_line)

    os.remove(current_dir+filename)
