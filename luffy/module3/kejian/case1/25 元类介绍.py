#储备知识exec
#参数1：字符串形式的命令
#参数2：全局作用域(字典形式)，如果不指定默认就使用globals()
#参数3：局部作用域(字典形式)，如果不指定默认就使用locals()

# g={
#     'x':1,
#     'y':2
# }
#
# l={}
#
# exec("""
# global x,m
# x=10
# m=100
#
# z=3
# """,g,l)

# print(g)
# print(l)


#一切皆对象，对象可以怎么用？
#1、都可以被引用，x=obj
#2、都可以当作函数的参数传入
#3、都可以当作函数的返回值
#4、都可以当作容器类的元素，l=[func,time,obj,1]



#类也是对象,Foo=type(....)
# class Foo:
#     pass
#
# obj=Foo()
# print(type(obj))
# print(type(Foo))
#
#
# class Bar:
#     pass
#
# print(type(Bar))

#产生类的类称之为元类，默认所以用class定义的类，他们的元类是type

#定义类的两种方式：
#方式一：class
class Chinese: #Chinese=type(...)
    country='China'

    def __init__(self,namem,age):
        self.name=namem
        self.age=age

    def talk(self):
        print('%s is talking' %self.name)

# print(Chinese)
obj=Chinese('egon',18)
print(obj,obj.name,obj.age)
#方式二：type

#定义类的三要素:类名，类的基类们，类的名称空间
class_name='Chinese'
class_bases=(object,)

class_body="""
country='China'

def __init__(self,namem,age):
    self.name=namem
    self.age=age

def talk(self):
    print('%s is talking' %self.name)
"""

class_dic={}
exec(class_body,globals(),class_dic)
# print(class_dic)

Chinese1=type(class_name,class_bases,class_dic)
# print(Chinese1)

obj1=Chinese1('egon',18)
print(obj1,obj1.name,obj1.age)