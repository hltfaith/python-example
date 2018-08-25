'''
练习1：编写一个学生类，产生一堆学生对象， (5分钟)

要求：

有一个计数器（属性），统计总共实例了多少个对象
'''

class Student:
    school='luffycity'
    count=0

    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
        # self.count+=1
        Student.count+=1

    def learn(self):
        print('%s is learing' %self.name)


stu1=Student('alex','male',38)
stu2=Student('jinxing','female',78)
stu3=Student('egon','male',18)

#
# print(Student.count)
# print(stu1.count)
# print(stu2.count)
# print(stu3.count)
# print(stu1.__dict__)
# print(stu2.__dict__)
# print(stu3.__dict__)



'''
练习2：模仿LoL定义两个英雄类， (10分钟)

要求：

英雄需要有昵称、攻击力、生命值等属性；
实例化出两个英雄对象；
英雄之间可以互殴，被殴打的一方掉血，血量小于0则判定为死亡。
'''

class Garen:
    camp='Demacia'

    def __init__(self,nickname,life_value,aggresivity):
        self.nickname=nickname
        self.life_value=life_value
        self.aggresivity=aggresivity

    def attack(self,enemy):
        enemy.life_value-=self.aggresivity
        #r1.life_value-=g1.aggresivity

class Riven:
    camp = 'Noxus'

    def __init__(self, nickname, life_value, aggresivity):
        self.nickname = nickname
        self.life_value = life_value
        self.aggresivity = aggresivity

    def attack(self, enemy):
        enemy.life_value -= self.aggresivity

g1=Garen('草丛伦',100,30)

r1=Riven('可爱的锐雯雯',80,50)

print(r1.life_value)
g1.attack(r1)
print(r1.life_value)






