# class A:
#     __x=1 #_A__x=1
#
#     def __init__(self,name):
#         self.__name=name #self._A__name=name
#
#     def __foo(self): #def _A__foo(self):
#         print('run foo')
#
#     def bar(self):
#         self.__foo() #self._A__foo()
#         print('from bar')

# print(A.__dict__)
# print(A.__x)
# print(A.__foo)

# a=A('egon')
# a._A__foo()
# a._A__x

# print(a.__name) #a.__dict__['__name']
# print(a.__dict__)

# a.bar()

'''
这种变形的特点：
    1、在类外部无法直接obj.__AttrName
    2、在类内部是可以直接使用：obj.__AttrName
    3、子类无法覆盖父类__开头的属性
'''

# class Foo:
#     def __func(self): #_Foo__func
#         print('from foo')
#
#
# class Bar(Foo):
#     def __func(self): #_Bar__func
#         print('from bar')

# b=Bar()
# b.func()



# class B:
#     __x=1
#
#     def __init__(self,name):
#         self.__name=name #self._B__name=name


#验证问题一：
# print(B._B__x)

#验证问题二：
# B.__y=2
# print(B.__dict__)
# b=B('egon')
# print(b.__dict__)
#
# b.__age=18
# print(b.__dict__)
# print(b.__age)


#验证问题三：
# class A:
#     def foo(self):
#         print('A.foo')
#
#     def bar(self):
#         print('A.bar')
#         self.foo() #b.foo()
#
# class B(A):
#     def foo(self):
#         print('B.foo')
#
# b=B()
# b.bar()



class A:
    def __foo(self): #_A__foo
        print('A.foo')

    def bar(self):
        print('A.bar')
        self.__foo() #self._A__foo()

class B(A):
    def __foo(self): #_B__foo
        print('B.foo')

b=B()
b.bar()






