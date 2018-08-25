#多分支：被监测的代码块抛出的异常有多种可能性，并且我们需要针对每一种异常类型都定制专门的处理逻辑
# try:
#     print('===>1')
#     # name
#     print('===>2')
#     l=[1,2,3]
#     # l[100]
#     print('===>3')
#     d={}
#     d['name']
#     print('===>4')
#
# except NameError as e:
#     print('--->',e)
#
# except IndexError as e:
#     print('--->',e)
#
# except KeyError as e:
#     print('--->',e)
#
#
# print('====>afer code')


#万能异常：Exception,被监测的代码块抛出的异常有多种可能性，
# 并且我们针对所有的异常类型都只用一种处理逻辑就可以了，那就使用Exception
# try:
#     print('===>1')
#     # name
#     print('===>2')
#     l=[1,2,3]
#     l[100]
#     print('===>3')
#     d={}
#     d['name']
#     print('===>4')
#
# except Exception as e:
#     print('异常发生啦：',e)
#
# print('====>afer code')




# try:
#     print('===>1')
#     # name
#     print('===>2')
#     l=[1,2,3]
#     # l[100]
#     print('===>3')
#     d={}
#     d['name']
#     print('===>4')
#
# except NameError as e:
#     print('--->',e)
#
# except IndexError as e:
#     print('--->',e)
#
# except KeyError as e:
#     print('--->',e)
#
# except Exception as e:
#     print('统一的处理方法')
#
#
# print('====>afer code')

#其他结构
# try:
#     print('===>1')
#     # name
#     print('===>2')
#     l=[1,2,3]
#     # l[100]
#     print('===>3')
#     d={}
#     d['name']
#     print('===>4')
#
# except NameError as e:
#     print('--->',e)
#
# except IndexError as e:
#     print('--->',e)
#
# except KeyError as e:
#     print('--->',e)
#
# except Exception as e:
#     print('统一的处理方法')
#
# else:
#     print('在被检测的代码块没有发生异常时执行')
#
# finally:
#     print('不管被检测的代码块有无发生异常都会执行')
#
#
#
# print('====>afer code')


# try:
#     f=open('a.txt','r',encoding='utf-8')
#     print(next(f))
#     print(next(f))
#     print(next(f))
#     print(next(f))
#
#     print(next(f))
#     print(next(f))
# finally:
#     f.close()


#主动触发异常：raise  异常类型(值)
# class People:
#     def __init__(self,name,age):
#         if not isinstance(name,str):
#             raise TypeError('名字必须传入str类型')
#         if not isinstance(age,int):
#             raise TypeError('年龄必须传入int类型')
#
#         self.name=name
#         self.age=age
#
# p=People('egon',18)


#自定义异常类型
class MyException(BaseException):
    def __init__(self,msg):
        super(MyException,self).__init__()
        self.msg=msg

    def __str__(self):
        return '<%s>' %self.msg

raise MyException('我自己的异常类型') #print(obj)






#断言assert

# info={}
# info['name']='egon'
# # info['age']=18
#
#
#
#
#
#
# # if 'name' not in info:
# #     raise KeyError('必须有name这个key')
# #
# # if 'age' not in info:
# #     raise KeyError('必须有age这个key')
#
# assert ('name' in info) and ('age' in info)
#
#
#
# if info['name'] == 'egon' and info['age'] > 10:
#     print('welcome')












try:
    pass


except Exception:
    pass







