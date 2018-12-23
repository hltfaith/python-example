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


3.__len__ len(obj)
obj对应的类中含有__len__方法，len(obj)才能正常执行

4.__hash__ hash(obj)  

只有实现了__hash__方法，hash(ojb)才能正常执行
hash是加加速寻址
print(hash('str'))
执行输出： 8500378945365862541

hash之后的数字，就是内存地址
hash之后，将value存储在对应的内存地址中

字典占用的内存相对的比，较用空间换时间
list占用的内存比较少，但是没有字典快

过一分钟，再次查看，发现数据都变了
-8079646337729346465

5.__str__
改变对象的字符串显示
class A:
    def __init__(self,*args):
        self.args = list(args)
    def __str__(self):
        return '[%s]' % (','.join([str(i) for i in self.args]))
li = A(1,2,3,4,5)
print(li)  # 输出的结果是obj.__str__()的结果<br>print(str(li))  # 结果同上<br>print('%s'%li)  # 结果同上
执行输出：
[1,2,3,4,5]
[1,2,3,4,5]
每一个对象，都有__str__方法
print执行时，实际是调用了__str__方法


6.__repr__
















