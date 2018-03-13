
import os,sys
import json
import pickle

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core import uid

# 数据库模块
db_DIR = BASE_DIR + r"/db"
db_admin = BASE_DIR + r"/db/admin.json"

# 存储功能
class Baseclass(object):
    def __init__(self):
        pass

# 保存数据
    def save(self, type, dict):
        filename = uid.create_md()
        dict['uid'] = filename
        file_path = "%s/%s" %(db_DIR, type)
        ab_file = "%s/%s" %(file_path, filename)
        if os.path.isdir(file_path):
            with open(ab_file, "wb") as f:
                f.write(pickle.dumps(dict))
                if True:
                    print("-----", type, "创建成功", "-------")
                    for key in dict:
                        print(key, ":\t", dict[key])

# 写入数据
    def seek_list(self, type, list):
        filename = uid.create_md()
        file_path = "%s/%s" %(db_DIR, type)
        ab_file = "%s/%s" %(file_path, filename)
        if os.path.isdir(file_path):
            with open(ab_file, 'wb') as f:
                f.write(pickle.dumps(list))
                if True:
                    print("-------", type, "创建成功", "---------")
                    for i in list:
                        for key in i:
                            print(key, i[key])
                        print("\n")
        return True

# 打开文件
    def open(self, type):
        all_data = []
        db_path = "%s/%s" %(db_DIR, type)
        for i in os.listdir(db_path):
            if os.path.isfile(os.path.join(db_path, i)):
                db_file = os.path.join(db_path, i)
                with open(db_file, 'rb') as f:
                    file_dict = pickle.load(f)
                    all_data.append(file_dict)

        return all_data
        #print(all_data)

#aa = Baseclass()

#aa.open("class_record")

# 课程类
class Course(Baseclass):
    def __init__(self, course_name, course_period, course_prices):
        Baseclass.__init__(self)
        self.course_name = course_name
        self.course_period = course_period
        self.course_prices = course_prices

# 班级类
class Classes(Baseclass):
    def __init__(self, classes_name, classes_teacher, classes_course):
        Baseclass.__init__(self)
        self.classes_name = classes_name
        self.classes_teacher = classes_teacher
        self.classes_course = classes_course

# 学校类
class School(Baseclass):
    def __init__(self, school_name, school_address):
        Baseclass.__init__(self)
        self.school_name = school_name
        self.school_address = school_address

# 管理员类
class Admin(Baseclass):
    def __init__(self):
        pass

# 创建学校
    def create_school(self):
        print('''
******创建学校******
            ''')
        school_dict = {}
        school_name = input("校  名：")
        school_address = input("地  址：")
        s1 = School(school_name, school_address)
        school_dict["校名"] = s1.school_name
        school_dict["地址"] = s1.school_address
        Baseclass.save(self, "school", school_dict)

# 创建班级
    def create_classes(self):
        print('''
******创建班级******
            ''')
        classes_dict = {}
        classes_name = input("班级名：")
        classes_teacher = input("负责讲师：")
        classes_course = input("所学课程：")
        cs1 = Classes(classes_name, classes_teacher, classes_course)
        classes_dict["班级名"] = cs1.classes_name
        classes_dict["负责讲师"] = cs1.classes_teacher
        classes_dict["所学课程"] = cs1.classes_course
        Baseclass.save(self, "classes", classes_dict)

# 创建学员
    def create_student(self):
        print('''
******创建学员******
            ''')
        student_dict = {}
        student_name = input("学员姓名：")
        student_sex = input("学员性别：")
        student_school = input("所属学校：")
        student_classes = input("学员班级：")
        st1 = Student(student_name, student_sex, student_school, student_classes)
        student_dict["姓名"] = st1.student_name
        student_dict["性别"] = st1.student_sex
        student_dict["学校"] = st1.student_school
        student_dict["班级"] = st1.student_classes
        print(student_dict)
        Baseclass.save(self, "student", student_dict)

# 创建讲师
    def create_teacher(self):
        print('''
******创建讲师******
            ''')
        teacher_dict = {}
        teacher_name = input("讲师姓名：")
        teacher_salary = input("讲师工资：")
        teacher_school = input("所属学校：")
        t1 = Teachar(teacher_name, teacher_salary, teacher_school)
        teacher_dict["姓名"] = t1.teacher_name
        teacher_dict["工资"] = t1.teacher_salary
        teacher_dict["学校"] = t1.teacher_school
        print(teacher_dict)
        Baseclass.save(self, "teacher", teacher_dict)

# 创建课程
    def create_course(self):
        print('''
******创建课程******
            ''')
        course_dict = {}
        course_name = input("课程名：")
        course_period = input("周 期：")
        course_prices = input("价 格：")
        c1 = Course(course_name, course_period, course_prices)
        course_dict["课程名"] = c1.course_name
        course_dict["周期"] = c1.course_period
        course_dict["价格"] = c1.course_prices
        Baseclass.save(self, "course", course_dict)

# 讲师信息
    def info_tercher(self):
        teacher_name = input("讲师姓名：")
        teacher_data = Baseclass.open(self, 'teacher')
        for i in teacher_data:
            if i['姓名'] == teacher_name:
                print('''
------讲师信息------
讲   师：%s
所属学校：%s
                ''' %(i['姓名'], i['学校']))
            else:
                print("讲师姓名输入有误！")

# 学员信息
    def info_student(self):
        student_name = input("学员姓名：")
        student_data = Baseclass.open(self, 'student')
        for i in student_data:
            if i['姓名'] == student_name:
                print('''
        ------学员信息------
        学   员：%s
        所属学校：%s
                        ''' % (i['姓名'], i['学校']))
            else:
                print("学员姓名输入有误！")

# 课程信息
    def info_course(self):
        course_name = input("课程名：")
        course_data = Baseclass.open(self, 'course')
        for i in course_data:
            if i['课程名'] == course_name:
                print('''
                ------课程信息------
                课 程 名：%s
                周   期：%s
                价   格：%s
                                ''' % (i['课程名'], i['周期'], i['价格']))
            else:
                print("学员姓名输入有误！")

# 讲师类
class Teachar():
    def __init__(self, teacher_name, teacher_salary, teacher_school):
        Baseclass.__init__(self)
        self.teacher_name = teacher_name
        self.teacher_salary = teacher_salary
        self.teacher_school = teacher_school

# 创建学员上课记录
    def create_class_record(self):
        print('''
*******创建课程记录*******
            ''')
        class_record = []
        student_school = input("选择学校：")
        student_classes = input("选择班级：")
        student_times = input("课  次：")
        student_list = Baseclass.open(self, "student")
        for i in student_list:
            if i["学校"] == student_school and i["班级"] == student_classes:
                student_name = i["姓名"]
                student_status = input('%s 上课情况：' % student_name)
                i["上课情况"] = student_status
                i["课次"] = student_times
                class_record.append(i)
        Baseclass.seek_list(self, "class_record", class_record)

# 创建学员成绩
    def create_class_grade(self):
        print('''        
*******创建学员成绩*******
            ''')
        class_grade = []
        student_school = input("选择学校：")
        student_classes = input("选择班级：")
        student_times = input("课  次：")
        student_list = Baseclass.open(self, "student")
        for i in student_list:
            if i["学校"] == student_school and i["班级"] == student_classes:
                student_name = i["姓名"]
                student_grade = input("%s 成绩:" % student_name)
                i["成绩"] = student_grade
                i["课次"] = student_times
                class_grade.append(i)

        Baseclass.seek_list(self, "class_grade", class_grade)

# 查看学员成绩
    def teacher_view_grade(self):
        print('''        
*******上课表*******
            ''')
        grade_list = []
        student_school = input("校  名：")
        student_class = input("班  级：")
        student_times = input("课  次：")
        class_grade_list = Baseclass.open(self, "class_grade")
        for i in class_grade_list:
            for j in i:
                if j["学校"] == student_school and j["班级"] == student_class and j['课次'] == student_times:
                    grade_list.append(j)

        for i in grade_list:
            for key in i:
                print(key, i[key])
            print("\n")


# 查看学员上课记录

# 查看学员上课记录
    def teacher_view_record(self):
        print('''
******上课记录*******
        ''')
        record_list = []
        student_school = input("校  名：")
        student_class = input("班  级：")
        student_times = input("课  次：")
        class_record_list = Baseclass.open(self, "class_record")
        #print('----上课记录-----')
        for i in class_record_list:
            for j in i:
                if j["学校"] == student_school and j["班级"] == student_class and j["课次"] == student_times:
                    record_list.append(i)
                else:
                    print("没有相关的上课记录,请重新查找！")

        for i in record_list:
            for f in i:
                for key in f:
                    print(key, f[key])
                print("\n")

# 学员类
class Student(Baseclass):
    def __init__(self, student_name, student_sex, student_school, student_classes):
        Baseclass.__init__(self)
        self.student_name = student_name
        self.student_sex = student_sex
        self.student_school = student_school
        self.student_classes = student_classes

    def student_registered(self):
        student_dict = {}
        print('''
******欢迎进入学生注册系统*******
        ''')
        student_name = input("注册姓名：")
        student_sex = input("性   别：")
        student_school = input("学   校：")
        student_class = input("班   级：")
        st1 = Student(student_name, student_sex, student_school, student_class)
        student_dict["姓名"] = st1.student_name
        student_dict["性别"] = st1.student_sex
        student_dict["学校"] = st1.student_school
        student_dict["班级"] = st1.student_classes
        Baseclass.save(self, "studentu", student_dict)

    def student_pay_fees(self):
        print("交学费功能--未实现")

    def student_view_grade(self):
        print('''
******查看学员上课记录*******
            ''')
        student_school = input("校  名：")
        student_class = input("班  级：")
        student_times = input("课  次：")
        student_name = input("姓  名：")
        class_grade_list = Baseclass.open(self, "class_grade")
        for i in class_grade_list:
            for j in i:
                if j["学校"] == student_school and j["班级"] == student_class and j["课次"] == student_times and j["姓名"] == student_name:
                    for key in j:
                        print(key, j[key])
                    print("\n")

    def student_view_record(self):
        print('''
*******查看学员作业成绩********
            ''')
        student_school = input("校  名：")
        student_class = input("班  级：")
        student_times = input("课  次：")
        student_name = input("姓  名：")
        class_record_list = Baseclass.open(self, "class_record")
        for i in class_record_list:
            for j in i:
                if j["学校"] == student_school and j["班级"] == student_class and j["课次"] == student_times and j['姓名'] == student_name:
                    for key in j:
                        print(key, j[key])

                    print("\n")

# 学员视图类
class Student_view(Student):
    def __init__(self, student_name, student_sex, student_school, student_classes):
        Student.__init__(self, student_name, student_sex, student_school, student_classes)

    def login(self):
        student_dic = {
            '1': Student.student_registered,
            '2': Student.student_pay_fees,
            '3': Student.student_view_record,
            '4': Student.student_view_grade,
            '5': "logout"
        }

        if True:
            exit_flag = False
            while not exit_flag:
                print('''
*******欢迎进入学生视图**********
       1. 注册学员
       2. 交学费
       3. 查看上课记录
       4. 查看作业成绩
       5. 返回
                ''')
                choice = input("请输入功能编号：")
                if choice in student_dic:
                    if int(choice) == 5:
                        exit_flag = True
                    else:
                        student_dic[choice](self)
                else:
                    print("您输入的信息有误，请重新输入！")

# 讲师视图
class Teacher_view(Teachar):
    def __init__(self, teacher_name, teacher_salary, teacher_school):
        Teachar.__init__(self, teacher_name, teacher_salary, teacher_school)

    def login(self):

        teacher_dic = {
            '1': Teachar.create_class_record,
            '2': Teachar.create_class_grade,
            '3': Teachar.teacher_view_grade,
            '4': Teachar.teacher_view_record,
            '5': 'logout'
        }


        if True:
            exit_flag = False

            while not exit_flag:
                print('''
*******欢迎进入讲师视图*******
        1. 创建上课记录
        2. 创建学员成绩
        3. 查看学员成绩
        4. 查看学员上课记录
        5. 返回
                ''')

                choice = input('请输入功能编号：')
                if choice in teacher_dic:
                    if int(choice) == 5:
                        exit_flag = True
                    else:
                        teacher_dic[choice](self)
                else:
                    print("您输入的信息有误，请重新输入！")

# 管理员视图
class Admin_view(Admin):
    def __init__(self):
        pass

# 管理员密码认证
    def auth(self, username, password):
        if os.path.isfile(db_admin):
            with open(db_admin, 'r') as f:
                admin_date = json.load(f)
            if admin_date['name'] == username and admin_date['password'] == password:
                return True
                #print('success')
            else:
                print("用户名或密码错误！")

# 登陆
    def login(self):
        admin_dic = {
            '1': Admin_view.school_manager,
            '2': Admin_view.teacher_manager,
            '3': Admin_view.student_manager,
            '4': Admin_view.course_manager,
            '5': 'logout'
        }
        username = input('请输入用户名：')
        password = input('请输入密码：')
        auth = Admin_view.auth(self, username, password)
        if auth:
            exit_flag = False
            while not exit_flag:
                print('''
********欢迎进入管理员视图********
        1.校区管理
        2.讲师管理
        3.学生管理
        4.课程管理
        5.返回
                ''')
                choice = input('输入功能编号：')
                if choice in admin_dic:
                    if int(choice) == 5:
                        exit_flag = True
                    else:
                        print(admin_dic[choice])
                        admin_dic[choice](self)
                else:
                    print("您输入的信息有误，请重新输入！")

    def school_manager(self):
        exit_flag = False
        while not exit_flag:
            print('''
********欢迎进入校区管理********
        1.创建校区
        2.创建班级
        3.返回
            ''')
            choice = input('输入功能编号：')
            if int(choice) == 1:
                Admin.create_school(self)
            elif int(choice) == 2:
                Admin.create_classes(self)
            else:
                exit_flag = True

    def teacher_manager(self):
        exit_flag = False
        while not exit_flag:
            print('''
********欢迎进入讲师管理功能******
        1.创建讲师
        2.讲师信息
        3.返回
            ''')
            choice = input('输入功能编号：')
            if int(choice) == 1:
                Admin.create_teacher(self)
            elif int(choice) == 2:
                Admin.info_tercher(self)
            else:
                exit_flag = True

    def student_manager(self):
        exit_flag = False
        while not exit_flag:
            print('''
******欢迎进入学生管理功能******
        1.创建学员
        2.学员信息
        3.返回
            ''')
            choice = input('输入功能编号：')
            if int(choice) == 1:
                Admin.create_student(self)
            elif int(choice) == 2:
                Admin.info_student(self)
            else:
                exit_flag = True

    def course_manager(self):
        exit_flag = False
        while not exit_flag:
            print(''''
*******欢迎进入课程管理功能********
        1.创建课程
        2.课程信息
        3.返回
            ''')
            choice = input('输入功能编号：')
            if int(choice) == 1:
                Admin.create_course(self)
            elif int(choice) == 2:
                Admin.info_course(self)
            else:
                exit_flag = True

# 系统菜单
class menu(object):
    def __init__(self):
        pass

    def menu_system(self):

        menu_dic = {'1': Student_view, '2': Teacher_view, '3': Admin_view, '4': 'logout'}

        menu_input = '''
********欢迎进入选课系统*********
        1. 学员视图
        2. 讲师视图
        3. 管理员视图
        4. 退出
            '''
        menu_tage = False
        while not menu_tage:
            print(menu_input)
            choice = input('请输入功能编号：').strip()
            if choice in menu_dic:
                if int(choice) == 4:
                    menu_tage = True
                else:
                    menu_dic[choice].login(self)
            else:
                print('您输入的信息有误，请重新输入！')
