#1、新式类

#2、经典类

#在python2中-》经典类：没有继承object的类，以及它的子类都称之为经典类
#
# class Foo:
#     pass
#
# class Bar(Foo):
#     pass
#
#
# #在python2中-》新式类：继承object的类，以及它的子类都称之为新式类
# class Foo(object):
#     pass
#
# class Bar(Foo):
#     pass


#在python3中-》新式类：一个类没有继承object类，默认就继承object

# class Foo():
#     pass
# print(Foo.__bases__)


#验证多继承情况下的属性查找

class A:
    # def test(self):
    #     print('from A')
    pass

class B(A):
    # def test(self):
    #     print('from B')
    pass

class C(A):
    # def test(self):
    #     print('from C')
    pass

class D(B):
    # def test(self):
    #     print('from D')
    pass

class E(C):
    # def test(self):
    #     print('from E')
    pass

class F(D,E):
    # def test(self):
    #     print('from F')
    pass


#F,D,B,E,C,A

print(F.mro())
# f=F()
# f.test()





















