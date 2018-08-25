#1 什么是异常：异常是错误发生的信号，一旦程序出错，并且程序没有处理这个错误，那个就会抛出异常，并且程序的运行随之终止
#
# print('1')
# print('2')
# print('3')
# int('aaaa')
# print('4')
# print('5')
# print('6')

#2 错误分为两种：
#语法错误:在程序执行前就要立刻改正过来
# print('xxxx'
# if 1 > 2

#逻辑错误

#ValueError
# int('aaa')

#NameError
# name

#IndexError
# l=[1,2,3]
# l[1000]

#KeyError
# d={}
# d['name']


#AttributeError
# class Foo:
#     pass
#
# Foo.xxx


#ZeroDivisionError:
# 1/0


#TypeError:int类型不可迭代
# for i in 3:
#     pass

# import time
# time.sleep(1000)



#3 异常
#强调一：错误发生的条件如果是可以预知的，此时应该用if判断去预防异常
# AGE=10
# age=input('>>: ').strip()
#
# if age.isdigit():
#     age=int(age)
#     if age > AGE:
#         print('太大了')


#强调二：错误发生的条件如果是不可预知的，此时应该用异常处理机制，try...except
try:
    f=open('a.txt','r',encoding='utf-8')

    print(next(f),end='')
    print(next(f),end='')
    print(next(f),end='')
    print(next(f),end='')

    print(next(f),end='')
    print(next(f),end='')
    print(next(f),end='')

    f.close()
except StopIteration:
    print('出错啦')


print('====>1')
print('====>2')
print('====>3')

























