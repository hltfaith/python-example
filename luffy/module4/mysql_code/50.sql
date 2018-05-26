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
select count(sid) from student;

#3.查询生物课程和物理课程成绩都及格的学生id和姓名
select score.student_id,student.sname from course,score,student where 
course.cid = score.course_id and student.sid = score.student_id  and score.score >=60;

#4.查询每个年级的班级数,取出班级数最多的三个年级
select gname from class_grade,class where class_grade.gid = class.grade_id 
group by class.grade_id order by count(grade_id) desc limit 3;

#5.查询平均成绩最高和最低的学生的ID和姓名以及平均成绩
select student.sid,student.sname,avg(score) from student,score where student.sid = score.student_id group by score order by avg(score) limit 1;
select student.sid,student.sname,avg(score) from student,score where student.sid = score.student_id group by score order by avg(score) desc limit 1;

#6.查询每个年级的学生人数
select gname,count(gid) from student,class_grade where student.class_id = class_grade.gid group by class_grade.gname;

#7.查询每位学生的学号，姓名，选课数，平均成绩
select student.sid,student.sname,count(score.course_id),avg(score.score) from student,score 
where student.sid = score.student_id group by score.student_id;

#8.查询学生编号为2的学生的姓名，该学生成绩最高的课程名，成绩最低的课程名及分数
select student.sname,course.cname from student,score,course where score.student_id=student.sid 
and score.course_id=course.cid and student.sid=2 order by score desc limit 1;
select student.sname,course.cname,score.score from student,score,course where score.student_id=student.sid 
and score.course_id=course.cid and student.sid=2 order by score asc limit 1;

#9.查询姓李的老师的个数和所带班级数
select (select count(tea.tid) from teacher tea where tea.tname like '李%') as 姓李的人数,count(tea2.tid) as 课程 from teach2cls tea2
    where tea2.tid in (select tea.tid from teacher tea where tea.tname like '李%') group by tea2.tid;

#10.查询班级数小于5的年级id和年级名
select gid,gname from class_grade where gid in (select grade_id from class group by grade_id having count(class.grade_id)<5);

#11.查询班级信息，包括班级id、班级名称、年级级别(12为低年级,34为中年级,56为高年级)
select cid "班级id", caption "班级名称", gname "年级" from class left join class_grade on class.grade_id = class_grade.gid;

#12.查询学过“张三”老师2门课以上的同学的学号、姓名；
select sc.student_id,su.sname,count(sc.course_id) as class_sum from
score sc left join student su on sc.student_id = su.sid
where sc.course_id in 
(select co.cid as cid from teacher tc left join course co on tc.tid = co.teacher_id where tc.tname="张三")
group by sc.student_id
having class_sum >= 2;

#13.查询教授课程超过2门的老师的id和姓名；
select * from teacher where tid in
(select tid from teach2cls group by tid having count(cid)>=2);

#14.查询学过编号"1"课程和编号"2"的同学的学号、姓名；
select student.sid,student.sname from student,score,course 
where score.student_id=student.sid and score.course_id=course.cid and cid=1;

select student.sid,student.sname from student,score,course 
where score.student_id=student.sid and score.course_id=course.cid and cid=2;

#15.查询没有带过高年级的老师id和姓名;

#16.查询学过"张三"老师所教的所有课的同学的学号、姓名;
select sid,sname from student where sid in 
(   select student_id from score where course_id in 
        (select cid from course left join teacher on course.teacher_id = teacher.tid where
            teacher.tname = "张三"
        )
);

#17.查询带过超过2个班级的老师的id姓名;
select distinct tc.tid, tc.tname from teacher tc
left join course co on tc.tid = co.teacher_id
left join teach2cls t2c on t2c.cid = co.cid
group by t2c.cid
having count(tc.tid) >= 2;

#18.查询课程编号"2"的成绩比课程编号"1"课程低的所有同学的学号、姓名;
select sid,sname from student where sid in 
(
    select a.sid from (select * from score s where s.course_id = 1)a,
    (select * from score s where s.course_id = 2)b
    where a.student_id = b.student_id and a.score > b.score
);

#19.查询所带班级数最多的老师id和姓名;
select tc.tname, tc.tid from teacher tc 
left join teach2cls t2c on tc.tid = t2c.tid
group by t2c.tid order by count(cid) desc limit 1;

#20.查询有课程成绩小于60分的同学的学号、姓名；
select student.sid,student.sname from student left join score
on student.sid = score.student_id where score.score < 60;

#21.查询没有学全所有课的同学的学号、姓名;
select sid,sname from student st where
(select count(*) from score sc where st.sid = sc.student_id)<
(select count(*) from course);

#22.查询至少有一门课与学员为"1"的同学所学相同的同学的学号和姓名;
select distinct st.sid,st.sname from student st inner join score sc on 
st.sid = sc.student_id where sc.course_id in 
(select course_id from score where student_id='1');


#23.查询至少学过学号为1同学所选课程中任意一门课的其他同学学号和姓名;
select distinct st.sid,st.sname from student st inner join score sc on
st.sid=sc.student_id where st.sid <> 1 and sc.course_id in 
(select course_id from score where student_id='1');

#24.查询和2号同学学习的课程完全相同的其他同学的学号和姓名;
SELECT sid,sname FROM student

WHERE sid NOT IN (

    SELECT 2

    UNION

    SELECT s1.sid FROM (SELECT course_id FROM score WHERE student_id = 2) AS sc,

    student s1

    WHERE NOT EXISTS (

        SELECT 1 FROM score AS s

        WHERE s.course_id = sc.course_id AND s1.sid = s.student_id

    )

);

#25.删除学习张三老师课的score标记录；
delete from score where course_id in 
    (select cid from course left join teacher on course.teacher_id = teacher.tid where teacher.tname = '张三');


#26.向score表中插入一些记录，这些记录要求符合以下条件:1没有上过编号2课程的同学学号;2插入2号课程的平均成绩;
insert into score select null,sid,2,(select avg(score) from score where course_id=2)
from student where sid not in (select distinct student_id from score where course_id=2);

#27.按平均成绩从低到高显示所有学生的"语文","数学","英语"三门的课程成绩,按如下形式显示:学生ID,语文,数学,英语,有效课程数，有效平均分;
select concat("学生ID: ",st.sid," ","课程ID: ",sc.course_id," ","平均成绩: ",avg(sc.score))
from student as st right join score as sc on st.sid = sc.student_id group by student_id;


#28.查询各科成绩最高和最低的分:以如下形式显示:课程ID,最高分，最低分;
select concat("课程ID",course_id,",","最高分 ",score,",","最低分")
from score group by course_id order by score desc limit 1;


#29.按各科平均成绩从低到高和及格率的 百分数从高到低顺序;
select * from score group by course_id order by avg(score) desc;

#30.课程平均分从高到低显示(现实任课老师)
select tname,cname,score from teacher right join (
select cname,score,teacher_id from score left join course on score.course_id = course.cid
group by course_id order by avg(score) desc) as tmp on tmp.teacher_id = teacher.tid;

#31.查询各科成绩前三名的记录(不考虑成绩并列情况)
select * from student right join score on student.sid = score.student_id 
group by course_id order by score desc limit 3;

#32.查询每门课程被选修的学生数
select cname "课程",count(student_id) "选修学生总数" from score left join
    course on score.course_id = course.cid group by course_id;

#33.查询选修了2门以上课程的全部学生的学号和姓名;
select sid,sname from student where sid in (
    select sid from score group by course_id having count(course_id) > 2
);

#34.查询男生,女生的人数,按到序排列;
select gender "性别", count(sid) "总人数" from student group by gender order by count(sid) desc;

#35.查询姓张的学生名单;
select * from student where sname like "张%";

#36.查询同名同性学生名单，并统计同名人数;
select sname "姓名",count(sid) "总人数" from student group by sname having count(sid) > 1;

#37.查询每门课程的平均成绩，结果按平均成绩升序排列,平均成绩相同时，按课程号将序排列;
select course_id,avg(score) from score group by course_id order by score asc;

#38.查询课程名为"数学",且分数低于60的学生名和分数;
select sname,score from student inner join score on score.sid = student.sid where score.score < 60;

#39.查询课程编号为"3"且课程成绩在80分以上的学生的学号和姓名;
select sid,sname from student where sid in
(select student_id from score where score.course_id = 2 and score.score > 80);

#40.求选修了课程的学生人数
select count(student_id) from score;

#41.查询选修王五老师所授权课程的学生中,成绩最高和最低的学生姓名及其成绩;


#42.查询各个课程及相应的选修人数;
select cname,count(sid) from course left join score on course.cid = score.course_id group by course_id;

#43.查询不同课程但成绩相同的学生的学号,课程号,学生成绩;
select sid,sname from student where sid in (
    select a.student_id from score a left join score b on
    a.course_id <> b.course_id where a.score = b.score
);

#44.查询每门课程成绩最好的前两名学生id和姓名;


#45.检索至少选修两门课程的学生学号
select sid "学生序号" from score group by course_id having count(*)>=2;

#46.查询没有学生选修的课程号和课程名
select cid, cname from course where cid not in (select course_id from score);

#47.查询没带过任何班级的老师id和姓名
select * from teacher where tid not in (select tid from teach2cls);

#48.查询有两门以上课程超过80分的学生id及其平均成绩;
select student_id "学生ID",avg(score) "平均成绩" from score where score>60 
group by course_id having count(*)>=2;

#49.检索3课程分数小于60,按分数将序排列的同学学号；
select sid from student where sid in (
    select student_id from score where score < 60 and course_id=2 order by score desc
);

#50.删除编号为2的同学的1课程的成绩;
delete from score where course_id = 1 and student_id = 2;

#51.查询同时选修了物理课和生物课的学生id和姓名;
select student.sid,student.sname from course,student where course.cname="生物" and course.cname="物理";
