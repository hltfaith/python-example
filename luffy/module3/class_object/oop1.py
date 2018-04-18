
'''
# 多态特性
import abc
class Animal(metaclass=abc.ABCMeta): #同一类事物:动物
    @abc.abstractmethod
    def talk(self):
        pass

class People(Animal): #动物的形态之一:人
    def talk(self):
        print('say hello')

class Dog(Animal): #动物的形态之二:狗
    def talk(self):
        print('say wangwang')

class Pig(Animal): #动物的形态之三:猪
    def talk(self):
        print('say aoao')

def func(obj):
    obj.talk()

'''


'''
# 封装
class show():
    def __fa(self):
        print('fengzhuang')

    def test(self):
        self.__fa()

class client(show):
    def __fa(self):
        print('client')
    def test(self):
        self.__fa()

# a = client()
# a.test()

class yuan():
    def fa(self):
        print('fengzhuang')

    def test(self):
        self.fa()

class client1(yuan):
    def fa(self):
        print('client')

a = client1()
a.test()

'''

'''
# 封装数据

class Teacher:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def tell_info(self):
        print('姓名:%s,年龄:%s' %(self.__name,self.__age))
    def set_info(self,name,age):
        if not isinstance(name,str):
            raise TypeError('姓名必须是字符串类型')
        if not isinstance(age,int):
            raise TypeError('年龄必须是整型')
        self.__name=name
        self.__age=age

t=Teacher('egon',18)
t.tell_info()

t.set_info('egon',19)
t.tell_info()

'''

'''
# 特性（property）
# 
# property是一种特殊的属性，访问它时会执行一段功能（函数）然后返回值

class People:
    def __init__(self,name,weight,height):
        self.name=name
        self.weight=weight
        self.height=height
    @property
    def bmi(self):
        return self.weight / (self.height**2)

p1=People('egon',75,1.85)
print(p1.bmi)

'''


'''
# 特性的扩展性
class Foo:
    def __init__(self, val):
        self.__name = val

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('%s must be str' % value)
        self.__name = value

    @name.deleter
    def name(self):
        raise TypeError('Can not delete')

f = Foo(1.0)
print(f.name)
# f.name = 10           # 抛出异常

del f.name

'''


'''
classmethod与staticmethod的对比

import settings
class MySQL:
    def __init__(self,host,port):
        self.host=host
        self.port=port

    @staticmethod
    def from_conf():
        return MySQL(settings.HOST,settings.PORT)

    # @classmethod #哪个类来调用,就将哪个类当做第一个参数传入
    # def from_conf(cls):
    #     return cls(settings.HOST,settings.PORT)

    def __str__(self):
        return '就不告诉你'

class Mariadb(MySQL):
    def __str__(self):
        return '<%s:%s>' %(self.host,self.port)


m=Mariadb.from_conf()
print(m) #我们的意图是想触发Mariadb.__str__,但是结果触发了MySQL.__str__的执行，打印就不告诉你：

'''
