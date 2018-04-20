
'''

# __getattr__ 用法

class aa():
    def __init__(self, x):
        self.x = x

    def __getattr__(self, item):
        print('exec getattr')

a = aa(1)
# print(a.x)   # 显示 1
print(a.xxxx)  # 显示 exec getattr

'''


'''
# __getattribute__ 用法 

class Foo:
    def __init__(self, x):
        self.x = x

    def __getattribute__(self, item):
        print('不管是否存在,我都会执行')

f1=Foo(10)
print(f1.x)
#print(f1.xxxxxx)

'''


'''

# __get__、__set__、__delete__用法

class Foo:
    def __get__(self, instance, owner):
        print('触发get')
    def __set__(self, instance, value):
        print('触发set')
    def __delete__(self, instance):
        print('触发delete')


a = Foo()
a.name = 'a'
print(a.name)

'''



'''

class Foo():
    def func(self):
        print('可以打印了哈哈')

a = Foo()
a.func()

# print(dir(Foo.func))

print(a.__dict__)
print(hasattr(Foo.func, '__set__'))
print(hasattr(Foo.func, '__get__'))
print(hasattr(Foo.func, '__delete__'))

'''

'''
# 小试牛刀
class Str:
    def __init__(self,name):
        self.name=name
    def __get__(self, instance, owner):
        print('get--->',instance,owner)
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print('set--->',instance,value)
        instance.__dict__[self.name]=value
    def __delete__(self, instance):
        print('delete--->',instance)
        instance.__dict__.pop(self.name)


class People:
    name=Str('name')
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

p1=People('egon',18,3231.3)

#调用
# print(p1.__dict__)
# print('------------------')
# print(p1.name)

# #赋值
# print(p1.__dict__)
# p1.name='egonlin'
# print(p1.__dict__)
#
# #删除
print(p1.__dict__)
del p1.name
print(p1.__dict__)
'''


'''

#拔刀相助

#疑问:如果我用类名去操作属性呢
#People.name #报错,错误的根源在于类去操作属性时,会把None传给instance

#修订__get__方法
class Str:
    def __init__(self,name):
        self.name=name
    def __get__(self, instance, owner):
        print('get--->',instance,owner)
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print('set--->',instance,value)
        instance.__dict__[self.name]=value
    def __delete__(self, instance):
        print('delete--->',instance)
        instance.__dict__.pop(self.name)

class People:
    name=Str('name')
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

print(People.name) #完美,解决
'''


'''

#磨刀霍霍
class Str:
    def __init__(self,name,expected_type):
        self.name=name
        self.expected_type=expected_type

    def __get__(self, instance, owner):
        print('get--->', instance, owner)
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print('set--->', instance, value)
        if not isinstance(value,self.expected_type): #如果不是期望的类型，则抛出异常
            raise TypeError('Expected %s' % str(self.expected_type))
        instance.__dict__[self.name]=value

    def __delete__(self, instance):
        print('delete--->',instance)
        instance.__dict__.pop(self.name)


class People:
    name=Str('name',str) #新增类型限制str
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

p1=People(123,18,3333.3)#传入的name因不是字符串类型而抛出异常
'''

'''
# 大刀阔斧
class Typed:
    def __init__(self,name,expected_type):
        self.name=name
        self.expected_type=expected_type
    def __get__(self, instance, owner):
        print('get--->',instance,owner)
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print('set--->',instance,value)
        if not isinstance(value,self.expected_type):
            raise TypeError('Expected %s' %str(self.expected_type))
        instance.__dict__[self.name]=value
    def __delete__(self, instance):
        print('delete--->',instance)
        instance.__dict__.pop(self.name)


class People:
    name=Typed('name',str)
    age=Typed('name',int)
    salary=Typed('name',float)
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

p1=People(123,18,3333.3)
p1=People('egon','18',3333.3)
p1=People('egon',18,3333)

'''


'''
# 类的装饰器:无参
def decorate(cls):
    print('类的装饰器开始运行啦------>')
    return cls

@decorate #无参:People=decorate(People)
class People:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

p1=People('egon',18,3333.3)
'''


'''
#类的装饰器:有参

def typeassert(**kwargs):
    def decorate(cls):
        print('类的装饰器开始运行啦------>',kwargs)
        return cls
    return decorate
@typeassert(name=str,age=int,salary=float) #有参:1.运行typeassert(...)返回结果是decorate,此时参数都传给kwargs 2.People=decorate(People)
class People:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

p1=People('egon',18,3333.3)
'''


'''
#终极大招
#刀光剑影

class Typed:
    def __init__(self,name,expected_type):
        self.name=name
        self.expected_type=expected_type
    def __get__(self, instance, owner):
        print('get--->', instance, owner)
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print('set--->',instance, value)
        if not isinstance(value,self.expected_type):
            raise TypeError('Expected %s' %str(self.expected_type))
        instance.__dict__[self.name]=value

    def __delete__(self, instance):
        print('delete--->',instance)
        instance.__dict__.pop(self.name)

def typeassert(**kwargs):
    def decorate(cls):
        print('类的装饰器开始运行啦------>',kwargs)
        for name,expected_type in kwargs.items():
            setattr(cls,name,Typed(name,expected_type))
        return cls
    return decorate
@typeassert(name=str,age=int,salary=float) #有参:1.运行typeassert(...)返回结果是decorate,此时参数都传给kwargs 2.People=decorate(People)

class People:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

print(People.__dict__)
p1=People('egon',18,3333.3)
'''
