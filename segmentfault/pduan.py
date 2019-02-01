import datetime
import os

'''
python 每天执行不同的列表,请问能用什么方法实现
'''

list_a = ['a','b','c','d','e','f','g','h','i','j','k']
list_b = ['A','B','C','D','E','F','G','H','I','J','K','L']

sum_list = ['list_a', 'list_b']
time = datetime.datetime.now().strftime('%Y-%m-%d')

if not os.path.isfile('db.txt'):
    open('db.txt', mode='w')

with open('db.txt', mode='r+', encoding='utf-8') as f:
    file = f.readlines()
    if len(file) == 0:
        f.write('%s,%s\n' % (time, sum_list[0]))
        print(list_a)
        exit()

with open('db.txt', mode='a+', encoding='utf-8') as d:
    for i in file:
        if time == i.strip('\n').split(',')[0]:
            print(eval(i.strip('\n').split(',')[1]))
            exit()

    if sum_list.index(file[-1].strip('\n').split(',')[1])+1 >= len(sum_list):
        d.write('%s,%s\n' % (time, sum_list[0]))
        print(list_a)
    else:
        d.write('%s,%s\n' % (time, sum_list[sum_list.index(file[-1].strip('\n').split(',')[1])+1]))
        print(eval(sum_list[sum_list.index(file[-1].strip('\n').split(',')[1])+1]))
