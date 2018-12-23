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
class Teacher:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):  # 重新定义内置方法
        return "Teacher's object %s" % self.name
 
    def __repr__(self):  # 重新定义内置方法，为了做个性化输出
        return 'repr function %s'%self.name
 
a = Teacher('alex',80)
b = Teacher('egon',80)
print(repr(a))  # 打印repr函数的返回值
print(a.__repr__()) #调用__repr__方法
print('%r'%a)
print(str(a)) # 打印str函数的返回值

执行输出：
repr function alex
repr function alex
repr function alex
Teacher's object alex

repr(obj)的结果和obj.__repr__()是一样的
'%r'%(obj)的结果和obj.__repr__()是一样的

所有的输出，本质就是向文件中写
print执行时，是去内部中寻找__str__方法
所以print没有输出不了的数据，因为每一个对象都有__str__方法
print一个对象是，打印的是内存地址

repr执行时，其实是调用__repr__方法
repr(obj)的结果和obj.__repr__()是一样的

概念：
那么repr是做了归一化设计，接收一个对象。python一切皆对象
每个对象都有__repr__方法。执行rept，就执行了__repr__方法。
为什么做归一化设计呢？因为要更接近于面向函数编程
如果每一个对象，都要对象名.__str__这样执行，太麻烦了

使用函数的方法，要比类名.方法名 使用简单
当需要使用__str__的场景时找不到 __str__就找__repr__
当需要使用__repr__的场景时找不到__repr__的时候就找父类的repr
双下repr是双下str的备胎

总结：

len() obj.__len__() 返回值是一致的
len() 的结果是依赖 obj.__len__()
hash() 的结果是依赖 obj.__hash__()

str() 的结果是依赖 obj.__str__()
print(obj) 的结果是依赖 obj.__str__()
%s 的结果是依赖 obj.__str__() 语法糖
repr() 的结果是依赖 obj.__repr__()
%r 的结果是依赖 obj.__repr__()
repr是str的备胎
如果__str__和__repr__同时存在， 一定是选择repr


7.__format__
format执行，就是调用了__format__方法
class A:
    def __init__(self,name,school,addr):
        self.name = name
        self.school = school
        self.addr = addr
 
    def __format__(self, format_spec):
        #format_spec = '{obj.name}-{obj.addr}-{obj.school}'
        return format_spec.format(obj=self) #此行的format_spec等同于上面一行
 
a = A('大表哥','oldboy','沙河')
format_spec = '{obj.name}-{obj.addr}-{obj.school}'
print(format(a,format_spec))

执行输出：
大表哥-沙河-oldboy


8.__call__
对象后面加括号，触发执行。
注：构造方法的执行是由创建对象触发的，即：对象 = 类名() ；而对于 __call__ 方法的执行是由对象后加括号触发的，即：对象() 或者 类()()
class Teacher():
    def __call__(self):
        print(123)
t = Teacher()
t()  # 对象名() 相当于调用类内置的__call__
Teacher()()  #效果同上

执行输出：
123
123


9.__eq__
__eq__ 定义了类的等号(==)行为
==实际是调用了 __eq__方法，它是判断内存地址，是否一致

自定义__eq__方法
class A:
    def __eq__(self, other):
        return True
a = A()
b = A()
a.name = 'alex'  # 增加一个属性
b.name = 'egon'
print(a == b)


10.__del__
析构方法，当对象在内存中被释放时，自动触发执行。
注：此方法一般无须定义，因为Python是一门高级语言，程序员在使用时无需关心内存的分配和释放，因为此工作都是交给Python解释器来执行，
所以，析构函数的调用是由解释器在进行垃圾回收时自动触发执行的。

class A:
    def __init__(self):
        pass
    def __del__(self):
        print('执行我啦')
 
a = A()
print('aaa')
执行输出：

aaa
执行我啦

当类执行完毕时，自动执行析构方法


11.__new__
__new__方法是创建类实例的方法，它的调用是发生在__init__之前的

它是一个静态方法，没有self，因为此刻还没有self
__new__()面试必考
先有对象，才能初始化
__new__方法不需要写，object自带

先来讲一个设计模式-->单例模式
如果面试中，只要 是问单例模式，就是问__new__
单例模式 就是一个类只能有一个实例

应用场景
1.当一个类，多次实例化时，每个实例都会占用资源，而且实例初始化会影响性能，这个时候就可以考虑使用单例模式，它给我们带来的好处是只有一个实例占用资源，
并且只需初始化一次
2.当有同步需要的时候，可以通过一个实例来进行同步控制，比如对某个共享文件（如日志文件）的控制，对计数器的同步控制等，这种情况下由于只有一个实例，
所以不用担心同步问题

看下面的代码：
class A:pass
a = A()
b = A()
print(a)
print(b)

执行输出：

<__main__.A object at 0x00000299A8D9BF28>
<__main__.A object at 0x00000299A8DA1320>

这不是单例模式，因为内存地址不一样
不是__init__的锅，是__new__的锅
__new__每次实例化，会创建一个新的内存地址

下面看一个真正的单例模式，使用__new__方法
class B:
    __instance = None
    def __new__(cls, *args, **kwargs):  # cls表示类
        if cls.__instance is None:  # 判断类变量__instance是否为None
            obj = object.__new__(cls)  # 创建一个实例对象
            cls.__instance = obj  # 赋值
        return cls.__instance  # 返回私有静态属性
 
a = B()
b = B()
print(a)
print(b)
执行输出：

<__main__.B object at 0x00000267F570BB00>
<__main__.B object at 0x00000267F570BB00>

上面的结果，内存地址是一样的。

注意：__new__每次实例化，都会执行！！！

实例化时，先执行__new__，再执行__init__

第一次执行时,cls.__instance 是None，创建一个对象
第二次执行时,cls.__instance 不是None，返回私有静态属性

 







