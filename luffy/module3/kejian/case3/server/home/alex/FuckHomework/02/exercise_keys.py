#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/6/15

"""
#练习一:
if True or False and False:
    print('yes')
else:
    print('no')
#输出结果为?为什么?

if (True or False) and False:
    print('yes')
else:
    print('no')

#输出结果为?为什么?
"""
# if True or False and False:
#     print('yes')
# else:
#     print('no')
#
# if (True or False) and False:
#     print('yes')
# else:
#     print('no')

"""
#练习二:编写if多分支,猜老男孩的年纪
"""

# age = 35
#
# user_input = input("猜猜看啊：").strip()  # 让用户输入猜的年龄
# user_input = int(user_input)  # input获取到的都是字符串类型，与int类型做比较需要转换成int类型
# if user_input > age:  # 如果猜的数比age大
#     print("大了！")
# elif user_input < age:  # 如果猜的数比age小
#     print("小了！")
# else:
#     print("对了！")  # 否则猜的数等于age

"""
#练习三:用户输入用户名密码验证,验证通过后进入子循环,输入命令,命令若为q,则退出所有循环
"""
# name = "Alex"
# password = "1234"
# exit_flag = False
#
# while not exit_flag:
#     input_n = input("请输入用户名：").strip()
#     input_p = input("请输入密码：").strip()
#     if input_n == name and input_p == password:
#         while not exit_flag:
#             input_cmd = input("请输入命令：").strip()
#             if input_cmd.upper() == "Q":
#                 exit_flag = True
#                 break
#     else:
#         print("用户名或密码错误！")
#         continue

"""
#练习四:循环取出元组中所有元素:
方式一:while和for(按照索引),
方式二:不按照索引的方式
# t=(1,2,3,4,5,6,7,8,9)
"""
t = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# 方法一
# n = 0
# while n < len(t):
#     print(t[n])
#     n += 1
#
# for i in range(len(t)):
#     print(t[i])

# 方法二
# for i in t:
#     print(i)

"""
#练习五:循环读取列表以及子列表中所有元素
l=[1,2,[3,4],[5,6]]
"""
# l = [1, 2, [3, 4], [5, 6]]
# for i in l:
#     # if type(i) == list:
#     if isinstance(i, list):
#         for j in i:
#             print(j)
#     else:
#         print(i)


# 练习六:打印
'''
   *
  ***
 *****
*******
'''

# for i in range(1, 8, 2):  # 1 3 5 7
#     print(("*" * i).center(7))
#
# for i in range(1, 8, 2):  # 1 3 5 7
#     print(' '*(4-(i+1)//2)+'*'*i)


# 练习七:打印
'''
 *****
  ***
   *
'''

# for i in range(5, 0, -2):  # 5 3 1
#     print(("*" * i).center(7))

# for i in range(5,0,-2):  # 5 3 1
#     print(' '*(4-(i+1)//2)+'*'*i)


# 练习八:打印
'''
*
**
***
****
*****
'''

# for i in range(1, 6):
#     print("*" * i)

# 练习九:打印
'''
******
*****
****
***
**
*
'''

# for i in range(5, 0, -1):
#     print("*" * i)

"""
#练习十:编写登陆接口
基础需求：
让用户输入用户名密码
认证成功后显示欢迎信息
输错三次后退出程序
"""

# username = "Alex"
# password = "1234"
# n = 3
# while n > 0:
#     input_n = input("请输入用户名：").strip()
#     input_p = input("请输入密码：").strip()
#
#     if input_n == username and input_p == password:
#         print("Hello Alex!")
#     else:
#         print("输入错误！")
#     n -= 1
# else:
#     print("输错三次，再见！")

"""
#数据类型练习题:
#练习一:有十进制数n=10
转成二进制
转成八进制
转成十六进制
"""
n = 10
# 转成二进制
n_2 = bin(10)

# 转成八进制
n_8 = oct(n)

# 转成十六进制
n_16 = hex(n)

"""
#练习二:与用户交互,要求用户输入年龄和薪资,
将用户输入的年龄转成整型,将用户输入的薪资转成浮点型
"""

# age = input("请输入年龄：").strip()
# salary = input("请输入薪资：").strip()
#
# age_int = int(age)  # 将年龄转换成整型
# salary = float(salary)  # 将薪资转成浮点型

"""
#练习三:
用户输入用户名,年纪,工作,爱好,格式化输出如下内容(使用%s和format两种方式)
------------ info of Alex Li -----------
Name  : Alex Li
Age   : 22
job   : Teacher
Hobbie: girl
------------- end -----------------
"""

# %s 方式
# s = """
# ------------ info of Alex Li -----------
# Name  : %s
# Age   : %s
# job   : %s
# Hobbie: %s
# ------------- end -----------------
# """

# name = input("请输入用户名：").strip()
# age = input("请输入年纪：").strip()
# job = input("请输入工作：").strip()
# hobbie = input("请输入爱好：").strip()
#
# print(s % (name, age, job, hobbie))


# format 方式
# s = """
# ------------ info of Alex Li -----------
# Name  : {}
# Age   : {}
# job   : {}
# Hobbie: {}
# ------------- end -----------------
# """
#
# name = input("请输入用户名：").strip()
# age = input("请输入年纪：").strip()
# job = input("请输入工作：").strip()
# hobbie = input("请输入爱好：").strip()
#
# print(s.format(name, age, job, hobbie))

"""
#练习四:
s='alex say hello'
切片取出say
切片取出倒数后两个字符
"""
# s = 'alex say hello'
# print(s[5:9])
# print(s[-2:])

"""
#练习五:
# 编写循环,让用户输入年纪,如果输入为空,或者不为数字,则重新输入
"""

# while True:
#     age = input("请输入年纪：").strip()
#
#     if age:  # 判断输入是否为空
#         if age.isdigit():  # 判断是不是数字
#             print("年纪：{}".format(int(age)))
#             break

"""
#练习六:
用列表模拟上电梯的流程(队列)
    循环生成一个1000个值的列表(入队)
    循环取走这个1000个值(出队)

"""

# q = []  # 定义一个列表
# for i in range(1000):
#     q.append(i)  # 入队
#
# for j in range(1000):
#     print(q[0])  # 依次出队
#
"""
用列表模拟把衣服放箱子里,然后取衣服的流程(堆栈)
    循环生成一个1000个值的列表(入栈)
    循环取走这个1000个值(出栈)
"""
# q = []
# for i in range(1000):
#     q.append(i)
#
# for j in range(1, 1001):
#     print(q[-j])

"""
#练习七：
dicta={'a':1,'b':2,'c':3,'d':'hello'}
dictb={'b':3,'c':2,'d':'world','f':10}
#两字典相加,不同的key对应的值保留,相同的key对应的值相加后保留,如果是字符串就拼接(字符串拼接'hello'+'world'得'helloworld')
# {'a': 1, 'b': 5, 'c': 5, 'd': 'helloworld', 'f': 10}
"""
# dicta = {'a': 1, 'b': 2, 'c': 3, 'd': 'hello'}
# dictb = {'b': 3, 'c': 2, 'd': 'world', 'f': 10}
#
# dic = {}  # 定义一个字典，存放最后的结果
# dic = dicta  # 先把dica的内容放到dic里
# for i in dictb:
#     if i in dic:  # 相同的key对应的值相加后保留
#         dic[i] += dictb[i]
#     else:  # 不同的key对应的值保留
#         dic[i] = dictb[i]
#
# print(dic)

"""
练习八:
a.实现用户输入用户名和密码,当用户名为seven且密码为123时,显示登录成功,否则登录失败!

b.实现用户输入用户名和密码,当用户名为seven且密码为123时,显示登录成功,否则登录失败,失败时允许重复输入三次

c.实现用户输入用户名和密码,当用户名为seven或alex且密码为123时,显示登录成功,否则登录失败,失败时允许重复输入三次
"""

# a、b 略，这里写个c的示例代码吧。。。不会偷懒的程序员就不是好助教。
# for i in range(3):
#     username = input("请输入用户名：").strip()
#     password = input("请输入密码：").strip()
#     # 判断，记得逻辑运算的优先级！！！先计算and再计算or，所以 'or' 这里要加个括号。
#     if (username.upper() == "ALEX" or username.upper() == "SEVEN") and password == "123":
#         print("登录成功！")
#     else:
#         print("用户名或密码错误！")

"""
练习九：
写代码

a.使用while循环实现输出2-3+4-5+6...+100的和
b.使用for循环和range实现输出1-2+3-4+5-6...+99的和
c.使用while循环实现输出1,2,3,4,5   7,8,9  11,12
d.使用while循环实现输出1-100内的所有奇数
e.使用while循环实现输出1-100内的所有偶数
"""
# a
a = 2  # 用a去模拟2 3 4 5 ... 100
ret_a = 0  # 结果放到ret_a
while a <= 100:
    if a % 2 == 0:  # 能被2整除就+
        ret_a += a
    else:
        ret_a -= a
    a += 1
print(ret_a)

# b
b = 1  # 用b去模拟1 2 3 4 5 ... 99
ret_b = 0  # 结果存放到ret_b
while b < 100:
    if b % 2 == 0:  # 能被2整除就-
        ret_b -= 1
    else:
        ret_b += 1
    b += 1
print(ret_b)

# c
c = 1
while c <= 12:
    if c == 6 or c == 10:
        c += 1
        continue
    else:
        print(c)
        c += 1

# d、e 略。。。

"""
练习十:
name = "alex"
a.移除name变量对应的值的两边的空格,并输出移除后的内容
b.判断name变量对应的值是否以"al"开头,并输出结果
c.判断name变量对应的值是否以"x"结尾,并输出结果
d.将name变量对应的值中的"l"替换为"p",并输出结果
e.将name变量对应的值根据"l"分割,并输出结果
f.请问,上一题e分割之后得到的值是什么类型
g.将name变量对应的值中变大写,并输出结果
h.将name变量对应的值中变小写,并输出结果
i.请输出name变量对应的值的第2个字符?
j.请输出name变量对应的值的前3个字符?
k.请输出name变量对应的值的后2个字符?
l.请输出name变量对应的值中"e"所在的索引位置?
"""

name = "alex"
# a
print(name.strip())

# b
print(name.startswith("al"))

# c
print(name.endswith("x"))

# d
print(name.replace("l", "p"))

# e
print(name.split("l"))

# f
print("list类型")

# g
print(name.upper())

# h
print(name.lower())

# i
print(name[1])

# j
print(name[:3])

# k
print(name[-2:])

# l
print(name.index("e"))

"""
练习十一:
写代码,有如下列表,按照要求实现每一个功能
li = ['alex','eric','rain','eric','rain']
a.计算列表长度并输出
b.列表中追加元素"seven",并输出添加后的列表
c.请在列表的第1个位置插入元素"Tony",并输出添加后的列表
d.请修改列表第2个位置的元素为"Kelly",并输出修改后的列表
e.请删除列表中的元素"eric",并输出修改后的列表
f.请删除列表中的第2个元素,并输出删除元素的值和删除元素后的列表
g.请删除列表中的第3个元素,并输出删除元素后的列表
h.请删除列表中的第2至4个元素,并输出删除元素后的列表
i.请将列表所有的元素反转,并输出反转后的列表
"""
li = ['alex', 'eric', 'rain', 'eric', 'rain']

# a
print(len(li))

# b
li.append("seven")  # 注意：append()操作的返回值是None，不是添加完元素的列表。能看到这里的都是天选之子。
print(li)

# c
li.insert(0, "Tony")  # insert()注意事项同上
print(li)

# d
li[1] = "Kelly"
print(li)

# e
li.remove("eric")
print(li)

# f
r = li[1]
li.remove(r)
print(li)

# g
li.remove(li[2])
print(li)

# h
del li[1:5]  # 这样快一些
li[1:5] = []  # 这样也行
print(li)

# i
li.reverse()  # 这样行，注意返回值是None
li[::-1]  # 这样也行，返回值就是反转后的新列表
print(li)

"""
#练习十二：
取出列表中的名字，年龄，出生的年，月，日
data=['alex',49,[1900,3,18]]
"""
data = ['alex', 49, [1900, 3, 18]]
print("名字：", data[0])
print("年龄：", data[1])
print("出生年：", data[2][0])
print("出生月：", data[2][1])
print("出生日：", data[2][2])

"""
#练习十三：
去掉重复
names=['egon','alex','egon','wupeiqi']
"""
names = ['egon', 'alex', 'egon', 'wupeiqi']
names = list(set(names))
names = ['egon', 'alex', 'egon', 'wupeiqi']
names = list(dict.fromkeys(names))  # 当然也可以利用字典的key不能重复来去重。能看到这里的就是尼玛天才
print(names)

"""
#练习十四：
去掉重复，且保证列表顺序与原来保持一致
names=['egon','alex','egon','wupeiqi']
"""
names = ['egon', 'alex', 'egon', 'wupeiqi']

# 两种方法
# 方法一：有序字典
from collections import OrderedDict
names = list(OrderedDict.fromkeys(names))
print(names)

# 方法二：利用set
seen = set()
names = [x for x in names if not (x in seen or seen.add(x))]
print(names)

"""
#练习十五：
去掉重复，且保证列表顺序与原来保持一致
names=[[1,2],3,[1,2],4]
"""

# 因为字典的key不能是列表，所以这里只能用上面的方法二了。

"""
#练习十六：
统计s='hello alex alex say hello sb sb'中每个单词的个数
"""
s = 'hello alex alex say hello sb sb'
s_l = s.split()  # 按空格分割成列表
keys = set(s_l)  # 取到所有出现过的单词
for i in keys:
    print(i, s_l.count(i))  # 打印下数量

"""
#练习十七：字典嵌套使用

Egon老师就是想让你们知道字典可以嵌套，可以用来做事情的。。。
"""



