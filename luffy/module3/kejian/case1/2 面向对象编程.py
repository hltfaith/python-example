'''
面向对象：核心就是对象二字，对象就是特征与技能的结合体
优点：可扩展性强
缺点：编程复杂度高
应用场景：用户需求经常变化，互联网应用，游戏，企业内部应用


类就是一系列对象相似的特征与技能的结合体
强调：站在不同的角度，得到的分类是不一样的

在现实世界中：一定先有对象，后有类
在程序中：一定得先定义类，后调用类来产生对象

站在路飞学院的角度，大家都是学生

在现实世界中：
    对象1：王二丫
        特征：
            学校='luffycity'
            名字='王二丫'
            性别='女'
            年龄=18
        技能：
            学习
            吃饭
            睡觉

    对象2：李三炮
        特征：
            学校='luffycity'
            名字='李三炮'
            性别='男'
            年龄=38
        技能：
            学习
            吃饭
            睡觉

    对象3：张铁蛋
        特征：
            学校='luffycity'
            名字='张铁蛋'
            性别='男'
            年龄=48
        技能：
            学习
            吃饭
            睡觉

    总结现实中路飞学院的学生类：
        相似的特征
            学校='luffycity'

        相似的技能
            学习
            吃饭
            睡觉


'''

#先定义类
class LuffyStudent:
    school='luffycity'

    def learn(self):
        print('is learning')

    def eat(self):
        print('is sleeping')


#后产生对象
stu1=LuffyStudent()
stu2=LuffyStudent()
stu3=LuffyStudent()

print(stu1)
print(stu2)
print(stu3)



























































