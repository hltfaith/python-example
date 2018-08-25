#python一切皆对象，在python3里统一类类与类型的概念


# print(type([1,2]))


# print(list)

class LuffyStudent:
    school='luffycity'

    def __init__(self,name,sex,age):
        self.Name=name
        self.Sex=sex
        self.Age=age

        #stu1.Name='王二丫'
        #stu1.Sex='女'
        #stu1.Age=18

    def learn(self,x):
        print('%s is learning %s' %(self.Name,x))

    def eat(self):
        print('%s is sleeping' %self.Name)


# print(LuffyStudent)


l1=[1,2,3] #l=list([1,2,3])
l2=[] #l=list([1,2,3])
# l1.append(4) #list.append(l1,4)
list.append(l1,4)
print(l1)