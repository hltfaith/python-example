
'''

#知识储备：
    #产生的新对象 = object.__new__(继承object类的子类)

#步骤一：如果说People=type(类名,类的父类们,类的名称空间)，那么我们定义元类如下，来控制类的创建
class Mymeta(type):  # 继承默认元类的一堆属性
    def __init__(self, class_name, class_bases, class_dic):
        if '__doc__' not in class_dic or not class_dic.get('__doc__').strip():
            raise TypeError('必须为类指定文档注释')

        if not class_name.istitle():
            raise TypeError('类名首字母必须大写')

        super(Mymeta, self).__init__(class_name, class_bases, class_dic)


class People(object, metaclass=Mymeta):
    country = 'China'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print('%s is talking' % self.name)

#步骤二：如果我们想控制类实例化的行为，那么需要先储备知识__call__方法的使用
class People(object,metaclass=type):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __call__(self, *args, **kwargs):
        print(self,args,kwargs)


# 调用类People，并不会出发__call__
obj=People('egon',18)

# 调用对象obj(1,2,3,a=1,b=2,c=3)，才会出发对象的绑定方法obj.__call__(1,2,3,a=1,b=2,c=3)
obj(1,2,3,a=1,b=2,c=3) #打印：<__main__.People object at 0x10076dd30> (1, 2, 3) {'a': 1, 'b': 2, 'c': 3}

#总结：如果说类People是元类type的实例，那么在元类type内肯定也有一个__call__，会在调用People('egon',18)时触发执行，然后返回一个初始化好了的对象obj

#步骤三：自定义元类，控制类的调用（即实例化）的过程
class Mymeta(type): #继承默认元类的一堆属性
    def __init__(self,class_name,class_bases,class_dic):
        if not class_name.istitle():
            raise TypeError('类名首字母必须大写')

        super(Mymeta,self).__init__(class_name,class_bases,class_dic)

    def __call__(self, *args, **kwargs):
        #self=People
        print(self,args,kwargs) #<class '__main__.People'> ('egon', 18) {}

        #1、实例化People，产生空对象obj
        obj=object.__new__(self)


        #2、调用People下的函数__init__，初始化obj
        self.__init__(obj,*args,**kwargs)


        #3、返回初始化好了的obj
        return obj

class People(object,metaclass=Mymeta):
    country='China'

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def talk(self):
        print('%s is talking' %self.name)

obj=People('egon',18)
print(obj.__dict__) #{'name': 'egon', 'age': 18}

#步骤四：
class Mymeta(type): #继承默认元类的一堆属性
    def __init__(self,class_name,class_bases,class_dic):
        if not class_name.istitle():
            raise TypeError('类名首字母必须大写')

        super(Mymeta,self).__init__(class_name,class_bases,class_dic)

    def __call__(self, *args, **kwargs):
        #self=People
        print(self,args,kwargs) #<class '__main__.People'> ('egon', 18) {}

        #1、调用self，即People下的函数__new__，在该函数内完成：1、产生空对象obj 2、初始化 3、返回obj
        obj=self.__new__(self,*args,**kwargs)

        #2、一定记得返回obj，因为实例化People(...)取得就是__call__的返回值
        return obj

class People(object,metaclass=Mymeta):
    country='China'

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def talk(self):
        print('%s is talking' %self.name)

    def __new__(cls, *args, **kwargs):
        obj=object.__new__(cls)
        cls.__init__(obj,*args,**kwargs)
        return obj

obj=People('egon',18)
print(obj.__dict__) #{'name': 'egon', 'age': 18}

#步骤五：基于元类实现单例模式,比如数据库对象,实例化时参数都一样,就没必要重复产生对象,浪费内存
class Mysql:
    __instance=None
    def __init__(self,host='127.0.0.1',port='3306'):
        self.host=host
        self.port=port

    @classmethod
    def singleton(cls,*args,**kwargs):
        if not cls.__instance:
            cls.__instance=cls(*args,**kwargs)
        return cls.__instance


obj1=Mysql()
obj2=Mysql()
print(obj1 is obj2) #False

obj3=Mysql.singleton()
obj4=Mysql.singleton()
print(obj3 is obj4) #True

#应用：定制元类实现单例模式
class Mymeta(type):
    def __init__(self,name,bases,dic): #定义类Mysql时就触发
        self.__instance=None
        super().__init__(name,bases,dic)

    def __call__(self, *args, **kwargs): #Mysql(...)时触发

        if not self.__instance:
            self.__instance=object.__new__(self) #产生对象
            self.__init__(self.__instance,*args,**kwargs) #初始化对象
            #上述两步可以合成下面一步
            # self.__instance=super().__call__(*args,**kwargs)

        return self.__instance
class Mysql(metaclass=Mymeta):
    def __init__(self,host='127.0.0.1',port='3306'):
        self.host=host
        self.port=port


obj1=Mysql()
obj2=Mysql()

print(obj1 is obj2)

'''


''''''
#练习题

# 练习一：在元类中控制把自定义类的数据属性都变成大写

class Mymetaclass(type):
    def __new__(cls,name,bases,attrs):
        update_attrs={}
        for k,v in attrs.items():
            if not callable(v) and not k.startswith('__'):
                update_attrs[k.upper()]=v
            else:
                update_attrs[k]=v
        return type.__new__(cls,name,bases,update_attrs)

class Chinese(metaclass=Mymetaclass):
    country='China'
    tag='Legend of the Dragon' #龙的传人
    def walk(self):
        print('%s is walking' %self.name)


print(Chinese.__dict__)
'''
{'__module__': '__main__',
 'COUNTRY': 'China', 
 'TAG': 'Legend of the Dragon',
 'walk': <function Chinese.walk at 0x0000000001E7B950>,
 '__dict__': <attribute '__dict__' of 'Chinese' objects>,                                         
 '__weakref__': <attribute '__weakref__' of 'Chinese' objects>,
 '__doc__': None}
'''
# 练习二：在元类中控制自定义的类无需init方法
#
#     1.元类帮其完成创建对象，以及初始化操作；
# 　　2.要求实例化时传参必须为关键字形式，否则抛出异常TypeError: must use keyword argument
# 　　3.key作为用户自定义类产生对象的属性，且所有属性变成大写

class Mymetaclass(type):
    # def __new__(cls,name,bases,attrs):
    #     update_attrs={}
    #     for k,v in attrs.items():
    #         if not callable(v) and not k.startswith('__'):
    #             update_attrs[k.upper()]=v
    #         else:
    #             update_attrs[k]=v
    #     return type.__new__(cls,name,bases,update_attrs)

    def __call__(self, *args, **kwargs):
        if args:
            raise TypeError('must use keyword argument for key function')
        obj = object.__new__(self) #创建对象，self为类Foo

        for k,v in kwargs.items():
            obj.__dict__[k.upper()]=v
        return obj

class Chinese(metaclass=Mymetaclass):
    country='China'
    tag='Legend of the Dragon' #龙的传人
    def walk(self):
        print('%s is walking' %self.name)


p=Chinese(name='egon',age=18,sex='male')
print(p.__dict__)
