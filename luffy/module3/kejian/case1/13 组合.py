
class People:
    school='luffycity'

    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex


class Teacher(People):
    def __init__(self,name,age,sex,level,salary,):
        super().__init__(name,age,sex)

        self.level=level
        self.salary=salary


    def teach(self):
        print('%s is teaching' %self.name)


class Student(People):
    def __init__(self, name, age, sex, class_time,):
        super().__init__(name,age,sex)

        self.class_time=class_time

    def learn(self):
        print('%s is learning' % self.name)

class Course:
    def __init__(self,course_name,course_price,course_period):
        self.course_name = course_name
        self.course_price = course_price
        self.course_period = course_period

    def tell_info(self):
        print('课程名<%s> 课程价钱<%s> 课程周期<%s>' %(self.course_name,self.course_price,self.course_period))

class Date:
    def __init__(self,year,mon,day):
        self.year=year
        self.mon=mon
        self.day=day

    def tell_info(self):
        print('%s-%s-%s' %(self.year,self.mon,self.day))

# teacher1=Teacher('alex',18,'male',10,3000,)
# teacher2=Teacher('egon',28,'male',30,3000,)
# python=Course('python',3000,'3mons')
# linux=Course('linux',2000,'4mons')

# print(python.course_name)

# teacher1.course=python
# teacher2.course=python

# print(python)
# print(teacher1.course)
# print(teacher2.course)
# print(teacher1.course.course_name)
# print(teacher2.course.course_name)
# teacher1.course.tell_info()

# student1=Student('张三',28,'female','08:30:00')
# student1.course1=python
# student1.course2=linux

# student1.course1.tell_info()
# student1.course2.tell_info()
# student1.courses=[]
# student1.courses.append(python)
# student1.courses.append(linux)



student1=Student('张三',28,'female','08:30:00')
d=Date(1988,4,20)
python=Course('python',3000,'3mons')


student1.birh=d
student1.birh.tell_info()

student1.course=python

student1.course.tell_info()
















