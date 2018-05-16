##############################################
##         创建数据库                          #
##############################################


#创建school数据库
create database school charset utf8;
use school;

#创建class表
create table class(
    cid int unique auto_increment,
    caption varchar(20) not null,
    grade_id int not null,
    primary key(cid)
);

#创建student表
create table student(
    sid int unique auto_increment,
    sname varchar(20) not null,
    gender enum("男", "女") not null default "男",
    class_id int not null,
    primary key(sid)
);

#创建teacher老师表
create table teacher(
    tid int unique auto_increment,
    tname varchar(20) not null,
    primary key(tid)
);

#创建course课程表
create table course(
    cid int unique auto_increment,
    cname varchar(20) not null,
    teacher_id int not null,
    primary key(cid)
);

#创建score成绩表
create table score(
    sid int unique auto_increment,
    student_id int not null,
    course_id int not null,
    score int(30) not null,
    primary key(sid)
);

#创建class_grade年级表
create table class_grade(
    gid int unique auto_increment,
    gname varchar(20) not null,
    primary key(gid)
);

#创建teach2cls任职表
create table teach2cls(
    tcid int unique auto_increment,
    tid int not null,
    cid int not null,
    primary key(tcid)
);

##############################################
##         插入数据                           #
##############################################


#插入class班级表数据
insert into class(caption, grade_id) values
    ("一年一班",1),
    ("二年一班",2),
    ("三年一班",3),
    ("一年二班",1),
    ("二年二班",2),
    ("三年二班",3),
    ("一年三班",1),
    ("二年三班",2),
    ("三年三班",3),
    ("四年一班",4),
    ("五年一班",5),
    ("六年一班",6),
    ("六年二班",6),
    ("六年三班",6),
    ("六年四班",6);

#插入student学生表数据
insert into student(sname, gender, class_id) values
    ("乔丹","女",1),
    ("艾弗森","女",1),
    ("科比","男",2);

#插入teacher老师表数据
insert into teacher(tname) values("张三"),("李四"),("王五");

#插入course课程表数据
insert into course(cname, teacher_id) values
    ("生物",1),
    ("体育",1),
    ("物理",2);

#插入score成绩表数据
insert into score(student_id, course_id, score) values
    (1,1,60),
    (1,2,59),
    (2,2,99);

#插入class_grade年级表数据
insert into class_grade(gname) values
    ("一年级"),
    ("二年级"),
    ("三年级"),
    ("四年级"),
    ("五年级"),
    ("六年级");

#插入teach2cls班级任职表数据
insert into teach2cls(tid,cid) values
    (1,1),
    (1,2),
    (2,1),
    (3,2);

##############################################
##         插入数据                           #
##############################################

#1. 自行创建测试数据
# 已完成

#2. 查询学生总人数
# select count(sid) from student;

#3.查询生物课程和物理课程成绩都及格的学生id和姓名
# select score.student_id,student.sname from course,score,student where course.cid = score.course_id and student.sid = score.student_id  and score.score >=60;

#4.查询每个年级的班级数,取出班级数最多的三个年级
# select gname from class_grade,class where class_grade.gid = class.grade_id group by class.grade_id order by count(grade_id) desc limit 3;

#5.查询平均成绩最高和最低的学生的ID和姓名以及平均成绩
#select student.sid,student.sname,avg(score) from student,score where student.sid = score.student_id group by score order by avg(score) limit 1;
#select student.sid,student.sname,avg(score) from student,score where student.sid = score.student_id group by score order by avg(score) desc limit 1;

#6.查询每个年级的学生人数
#select gname,count(gid) from student,class_grade where student.class_id = class_grade.gid group by class_grade.gname;

#7.查询每位学生的学号，姓名，选课数，平均成绩
#select student.sid,student.sname,count(score.course_id),avg(score.score) from student,score where student.sid = score.student_id group by score.student_id;

#8.查询学生编号为2的学生的姓名，该学生成绩最高的课程名，成绩最低的课程名及分数
#

#9.查询姓李的老师的个数和所带班级数
#

#10.查询班级数小于5的年级id和年级名








































