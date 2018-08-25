#在子类派生出的新的方法中重用父类的方法，有两种实现方式
#方式一：指名道姓（不依赖继承）
# class Hero:
#     def __init__(self,nickname,life_value,aggresivity):
#         self.nickname=nickname
#         self.life_value=life_value
#         self.aggresivity=aggresivity
#     def attack(self,enemy):
#         enemy.life_value-=self.aggresivity
#
#
# class Garen(Hero):
#     camp='Demacia'
#
#     def attack(self,enemy):
#         Hero.attack(self,enemy) #指名道姓
#         print('from Garen Class')
#
# class Riven(Hero):
#     camp='Noxus'
#
#
# g=Garen('草丛伦',100,30)
# r=Riven('锐雯雯',80,50)
#
# print(r.life_value)
# g.attack(r)
# print(r.life_value)




# class Hero:
#     def __init__(self,nickname,life_value,aggresivity):
#         self.nickname=nickname
#         self.life_value=life_value
#         self.aggresivity=aggresivity
#     def attack(self,enemy):
#         enemy.life_value-=self.aggresivity


# class Garen(Hero):
#     camp='Demacia'
#
#     def __init__(self,nickname,life_value,aggresivity,weapon):
#         # self.nickname=nickname
#         # self.life_value=life_value
#         # self.aggresivity=aggresivity
#         Hero.__init__(self,nickname,life_value,aggresivity)
#
#         self.weapon=weapon
#
#     def attack(self,enemy):
#         Hero.attack(self,enemy) #指名道姓
#         print('from Garen Class')
#
#
# g=Garen('草丛伦',100,30,'金箍棒')
#
# print(g.__dict__)




#方式二：super() (依赖继承)
# class Hero:
#     def __init__(self,nickname,life_value,aggresivity):
#         self.nickname=nickname
#         self.life_value=life_value
#         self.aggresivity=aggresivity
#     def attack(self,enemy):
#         enemy.life_value-=self.aggresivity
#
#
# class Garen(Hero):
#     camp='Demacia'
#
#     def attack(self,enemy):
#         super(Garen,self).attack(enemy) #依赖继承
#         print('from Garen Class')
#
# class Riven(Hero):
#     camp='Noxus'
#
#
# g=Garen('草丛伦',100,30)
# r=Riven('锐雯雯',80,50)
#
# g.attack(r)
# print(r.life_value)


# class Hero:
#     def __init__(self,nickname,life_value,aggresivity):
#         self.nickname=nickname
#         self.life_value=life_value
#         self.aggresivity=aggresivity
#     def attack(self,enemy):
#         enemy.life_value-=self.aggresivity
#
#
# class Garen(Hero):
#     camp='Demacia'
#
#     def __init__(self,nickname,life_value,aggresivity,weapon):
#         # self.nickname=nickname
#         # self.life_value=life_value
#         # self.aggresivity=aggresivity
#
#         # super(Garen,self).__init__(nickname,life_value,aggresivity)
#         super().__init__(nickname,life_value,aggresivity)
#         self.weapon=weapon
#
#     def attack(self,enemy):
#         Hero.attack(self,enemy) #指名道姓
#         print('from Garen Class')
#
#
# g=Garen('草丛伦',100,30,'金箍棒')
#
# print(g.__dict__)








class A:
    def f1(self):
        print('from A')
        super().f1()


class B:
    def f1(self):
        print('from B')

class C(A,B):
    pass


print(C.mro())
#[<class '__main__.C'>,
# <class '__main__.A'>,
# <class '__main__.B'>,
# <class 'object'>]


c=C()
c.f1()









