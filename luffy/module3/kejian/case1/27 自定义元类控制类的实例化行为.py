#知识储备__call__方法
# class Foo:
#     def __call__(self, *args, **kwargs):
#         print(self)
#         print(args)
#         print(kwargs)
#
#
# obj=Foo()
#
# obj(1,2,3,a=1,b=2,c=3) #obj.__call__(obj,1,2,3,a=1,b=2,c=3)
#
#
# #元类内部也应有有一个__call__方法，会在调用Foo时触发执行
# #Foo(1,2,x=1)  #Foo.__call__(Foo,1,2,x=1)




class Mymeta(type):
    def __init__(self,class_name,class_bases,class_dic):
        if not class_name.istitle():
            raise TypeError('类名的首字母必须大写')

        if '__doc__' not in class_dic or not class_dic['__doc__'].strip():
            raise TypeError('必须有注释，且注释不能为空')

        super(Mymeta,self).__init__(class_name,class_bases,class_dic)

    def __call__(self, *args, **kwargs): #obj=Chinese('egon',age=18)
        # print(self) #self=Chinese
        # print(args) #args=('egon',)
        # print(kwargs) #kwargs={'age': 18}

        #第一件事：先造一个空对象obj
        obj=object.__new__(self)
        #第二件事：初始化obj
        self.__init__(obj,*args,**kwargs)
        #第三件事：返回obj
        return obj

class Chinese(object,metaclass=Mymeta):
    '''
    中文人的类
    '''
    country='China'

    def __init__(self,namem,age):
        self.name=namem
        self.age=age

    def talk(self):
        print('%s is talking' %self.name)




obj=Chinese('egon',age=18) #Chinese.__call__(Chinese,'egon',18)

print(obj.__dict__)









