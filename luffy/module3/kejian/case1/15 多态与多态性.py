#多态：同一类事物的多种形态
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

class Cat(Animal):
    def talk(self):
        print('say miamiao')

#多态性：指的是可以在不考虑对象的类型的情况下而直接使用对象
peo1=People()
dog1=Dog()
pig1=Pig()
cat1=Cat()

# peo1.talk()
# dog1.talk()
# pig1.talk()

def func(animal):
    animal.talk()


func(peo1)
func(pig1)
func(dog1)
func(cat1)