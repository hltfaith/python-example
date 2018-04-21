
'''
# __doc__
# 它类的描述信息

class Foo:
    '我是描述信息'
    pass

print(Foo.__doc__)
# 该属性无法被继承

class Foo:
    '我是描述信息'
    pass

class Bar(Foo):
    pass
print(Bar.__doc__) #该属性无法继承给子类
'''


'''
# __module__和__class__
# __module__ 表示当前操作的对象在那个模块
# 
# __class__ 表示当前操作的对象的类是什么

lib/aa.py

class C:

    def __init__(self):
        self.name = ‘SB'

index.py

from lib.aa import C

obj = C()
print obj.__module__  # 输出 lib.aa，即：输出模块
print obj.__class__      # 输出 lib.aa.C，即：输出类

'''


'''
# __del__ 使用

# 析构方法，当对象在内存中被释放时，自动触发执行。
# 注：如果产生的对象仅仅只是python程序级别的（用户级），那么无需定义__del__,如果产生的对象的同时还会向操作系统
# 发起系统调用，即一个对象有用户级与内核级两种资源，比如（打开一个文件，创建一个数据库链接），则必须在清除对象的
# 同时回收系统资源，这就用到了__del__。

# 简单示范

class Foo:

    def __del__(self):
        print('执行我啦')

f1=Foo()
del f1
print('------->')

#输出结果
执行我啦
------->

# 挖坑埋了你

class Foo:

    def __del__(self):
        print('执行我啦')

f1=Foo()
# del f1
print('------->')

#输出结果
------->
执行我啦

# 典型的应用场景：
# 
# 创建数据库类，用该类实例化出数据库链接对象，对象本身是存放于用户空间内存中，而链接则是由操作系统管理的，存放于内核空间内存中
# 当程序结束时，python只会回收自己的内存空间，即用户态内存，而操作系统的资源则没有被回收，这就需要我们定制__del__，在对象被删
# 除前向操作系统发起关闭数据库链接的系统调用，回收资源
# 这与文件处理是一个道理：

f=open('a.txt') #做了两件事，在用户空间拿到一个f变量，在操作系统内核空间打开一个文件
del f #只回收用户空间的f，操作系统的文件还处于打开状态

#所以我们应该在del f之前保证f.close()执行,即便是没有del，程序执行完毕也会自动del清理资源，于是文件操作的正确用法应该是
f=open('a.txt')
#读写...
f.close()
#很多情况下大家都容易忽略f.close,这就用到了with上下文管理
'''


'''
# __enter__和__exit__ 使用
#我们知道在操作文件对象的时候可以这么写

with open('a.txt') as f:
　　'代码块'
# 上述叫做上下文管理协议，即with语句，为了让一个对象兼容with语句，必须在这个对象的类中声明__enter__和__exit__方法
#
# 上下文管理协议

class Open:
    def __init__(self,name):
        self.name=name

    def __enter__(self):
        print('出现with语句,对象的__enter__被触发,有返回值则赋值给as声明的变量')
        # return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('with中代码块执行完毕时执行我啊')


with Open('a.txt') as f:
    print('=====>执行代码块')
    # print(f,f.name)
#__exit__()中的三个参数分别代表异常类型，异常值和追溯信息,with语句中代码块出现异常，则with后的代码都无法执行
class Open:
    def __init__(self,name):
        self.name=name

    def __enter__(self):
        print('出现with语句,对象的__enter__被触发,有返回值则赋值给as声明的变量')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('with中代码块执行完毕时执行我啊')
        print(exc_type)
        print(exc_val)
        print(exc_tb)
        return True



with Open('a.txt') as f:
    print('=====>执行代码块')
    raise AttributeError('***着火啦,救火啊***')
print('0'*100) #------------------------------->会执行
#如果__exit()返回值为True,那么异常会被清空，就好像啥都没发生一样，with后的语句正常执行
'''



'''
#练习：模拟Open

class Open:
    def __init__(self,filepath,mode='r',encoding='utf-8'):
        self.filepath=filepath
        self.mode=mode
        self.encoding=encoding

    def __enter__(self):
        # print('enter')
        self.f=open(self.filepath,mode=self.mode,encoding=self.encoding)
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        # print('exit')
        self.f.close()
        return True
    def __getattr__(self, item):
        return getattr(self.f,item)

with Open('a.txt','w') as f:
    print(f)
    f.write('aaaaaa')
    f.wasdf #抛出异常，交给__exit__处理
# 用途或者说好处：
# 使用with语句的目的就是把代码块放入with中执行，with结束后，自动完成清理工作，无须手动干预
# 在需要管理一些资源比如文件，网络连接和锁的编程环境中，可以在__exit__中定制自动释放资源的机制，你无须再去关系这个问题，这将大有用处
'''


'''
# __call__ 使用

# 对象后面加括号，触发执行。 
# 注：构造方法的执行是由创建对象触发的，即：对象 = 类名() ；而对于 __call__ 方法的执行是由对象后加括号触发的，即：对象() 或者 类()()

class Foo:

    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        print('__call__')


obj = Foo() # 执行 __init__
obj()       # 执行 __call__
'''

