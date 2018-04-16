
'''
class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def zidingyi(self):
        print('%s喜欢看书,今年%s岁了！' % (self.name, self.age))

    def __del__(self):
        print('run __del__')


p = Person('changhao', '21')

print(p.__dict__)

'''

'''
练习1：编写一个学生类，产生一堆学生对象， (5分钟)

要求：

有一个计数器（属性），统计总共实例了多少个对象

参考博客：https://blog.csdn.net/a2011480169/article/details/73087097    （深入理解Python中的面向对象）

class Student:

    count = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.count += 1


a = Student('changhao', '18')
b = Student('changhao', '18')

print(Student.count)

'''


'''
练习2：模仿王者荣耀定义两个英雄类， (10分钟)

要求：

英雄需要有昵称、攻击力、生命值等属性；
实例化出两个英雄对象；
英雄之间可以互殴，被殴打的一方掉血，血量小于0则判定为死亡。

'''


'''
# MRO

class a():
    def a1(self):
        print('a1')

class b():
    def b1(self):
        print('b1')

class ab(a, b):
    def ab(self):
        print('ab')


# print(ab.mro())
'''


'''
# 在子类中调用父类的方法
# 方法一：指名道姓 调用父类，不依赖继承
class Vehicle: #定义交通工具类
     Country='China'
     def __init__(self,name,speed,load,power):
         self.name=name
         self.speed=speed
         self.load=load
         self.power=power

     def run(self):
         print('开动啦...')

class Subway(Vehicle): #地铁
    def __init__(self,name,speed,load,power,line):
        Vehicle.__init__(self,name,speed,load,power)
        self.line=line

    def run(self):
        print('地铁%s号线欢迎您' %self.line)
        Vehicle.run(self)

line13=Subway('中国地铁','180m/s','1000人/箱','电',13)
line13.run()


# 方法二： super()方法 调用父类，依赖继承

class traffic_tool():
    def __init__(self, name, car, num):
        self.name = name
        self.car = car
        self.num = num

    def run(self):
        print('%s地铁正在运行中.....' % self.name)


class beijing(traffic_tool):
    def __init__(self, name, car, num, line):
        super().__init__(name, car, num)
        self.line = line

    def run(self):
        print('地铁%s号线开通了....' % self.line)
        super(beijing, self).run()

bj = beijing('北京', '17', '1000', '10')
bj.run()

'''


'''
# 继承的实现原理
# python会计算出一个方法解析顺序(MRO)列表，这个MRO列表就是一个简单的所有基类的线性顺序列表
# 深度优先和广度优先

class A(object):
    def test(self):
        print('from A')

class B(A):
    def test(self):
        print('from B')

class C(A):
    def test(self):
        print('from C')

class D(B):
    def test(self):
        print('from D')

class E(C):
    def test(self):
        print('from E')

class F(D,E):
    # def test(self):
    #     print('from F')
    pass
f1=F()
f1.test()
print(F.__mro__) #只有新式才有这个属性可以查看线性列表，经典类没有这个属性

#新式类继承顺序:F->D->B->E->C->A
#经典类继承顺序:F->D->B->A->E->C
#python3中统一都是新式类
#pyhon2中才分新式类与经典类

'''


'''
# 组合与重用性
# 软件重用的重要方式除了继承之外还有另外一种方式，即：组合
# 
# 组合指的是，在一个类中以另外一个类的对象作为数据属性，称为类的组合

class weapon():
    def gun(self):
        print('杀伤力100')

class person(weapon):
    def __init__(self, name):
        self.name = name
        self.wuqi = weapon()

xiaoming = person('xiaoming')
xiaoming.wuqi.gun()


'''

'''
# 组合的方式
# 
# 用组合的方式建立了类与组合的类之间的关系，它是一种‘有’的关系,比如教授有生日，教授教python和linux课程，教授有学生s1、s2、s3...
# 
# 示例：继承与组合
# 老师、学生  课程

class person():
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

class course():
    def __init__(self, name, zhouqi, price):
        self.name = name
        self.zhouqi = zhouqi
        self.price = price

    def tell_info(self):
        print('课程名称%s,%s时间,%s元' % (self.name, self.zhouqi, self.price))

class Teacher(person):
    def __init__(self, name, age, sex, job):
        person.__init__(self, name, age, sex)
        self.job = job
        self.course = []
        self.student = []

class Student(person):
    def __init__(self, name, age, sex):
        person.__init__(self, name, age, sex)
        self.course = []

egon = Teacher('egon', '28', 'nan', 'teacher')
xiaoming = Student('xiaoming', '19', 'nan')


python = course('python', '2月', '20000')
linux = course('linux', '2月', '10000')

egon.course.append(python)
egon.course.append(linux)
egon.student.append(xiaoming)

xiaoming.course.append(linux)

for i in egon.course:
    i.tell_info()

'''
