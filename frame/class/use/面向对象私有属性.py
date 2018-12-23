面向对象的思想

    不关注程序执行的过程

    关心的是一个程序中的角色，以及角色与角色之间的关系

在python中，一切皆对象

1. __dict__
class Person:
    静态变量 = 123
 
print(Person.__dict__) #内置的双下划线方法

执行输出：
{'__doc__': None, '静态变量': 123, '__module__': '__main__', '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__dict__': <attribute '__dict__' of 'Person' objects>}

总结：

引用静态变量
  1.类名.__dict__['静态变量名'] 可以查看，但是不能删改
  2.类名.静态变量名 直接就可以访问,可以删改
  删除一个静态变量 del 类名.静态变量名

    
2. __dir__
class D:
    def __func(self):  # 变形为 _D__func
        print('in func')
class E(D):
    def __init__(self):
        pass
     
e = E()
print(e.__dir__())
查看当前范围内的变量、方法和定义的类型列表
执行输出：

['__ge__', '__gt__', '__new__', '__reduce_ex__', '__reduce__', '__dict__', '__le__', '__eq__', '__sizeof__', '__format__', '__getattribute__', '_D__func', '__hash__', '__str__', '__init__', '__module__', '__subclasshook__', '__weakref__', '__repr__', '__lt__', '__setattr__', '__ne__', '__class__', '__dir__', '__delattr__', '__doc__']


3.




