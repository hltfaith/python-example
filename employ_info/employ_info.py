# Version: python3.6.3
#  Author: Wu changhao

import os

# 表信息函数方法
def table_info():
    data_file = open('data.txt', 'r+')
    data = data_file.readlines()

    data_list = []
    for i in data:
        data_list.append(str(i).split(','))

    return data_list                                              # 将txt文本文件信息转换成一个数组，每次调用此方法将返回数组。


# 查询函数方法
def query():
    data_value = table_info()                                      # 调用表信息表信息函数方法
    input_query = input("请输入查询语句：")
    num1 = input_query[0:input_query.rfind('from', 0) + -1][5:]    # 截取 name,age格式
    num2 = input_query[input_query.rfind('>', 1) + 2:]             # 截取 age > 22
    num3 = input_query[input_query.rfind('where', 1) + 6:]         # 截取 dept = "IT"

    if num1 == '*':                                                # 判断查询语句，关键字是否为*号
        value = 'dept = "IT"'
        if value == num3:
            count = 0                                              # 计数器，每次加一
            for k in data_value:                                   # 遍历出来每个员工的信息
                if "IT" in k[4]:
                    str_i = ','.join(k).replace("\n", "")
                    str_ii = str_i.replace(',', " ")               # 将逗号替换成空格
                    print(str_ii)                                  # 打印出属于IT的员工信息
                    count += 1
            print("查询到%s条语句！" % count)                        # 打印出受影响的条数

        else:
            count = 0
            for k in data_value:
                if "2013" in k[5]:
                    str_i = ','.join(k).replace("\n", "")
                    str_ii = str_i.replace(',', " ")
                    print(str_ii)
                    count += 1
            print("查询到%s条语句！" % count)

    else:
        count = 0
        for k in data_value:
            if int(k[:][2]) > int(num2):
                print(k[1], k[2])
                count += 1
        print("查询到%d条语句！" % count)


# 新增函数方法
def add():
    data_value = table_info()

    input_add = input("请输入新增语句：")
    input_cut = input_add[16:]
    input_list = list(input_cut.split(','))

    phone_list = []                                             # 将已经存在的手机号，存在列表中
    for i in data_value:
        phone = i[3]
        phone_list.append(phone)

    if input_list[2] in phone_list:
        print('手机号已存在！')
        exit()

    else:
        data_count = (len(data_value)+1)                        # 设置新增员工的ID值
        input_list.insert(0, str(data_count))
        imput_list_str = ','.join(input_list)                   # 转换成以逗号分隔员工信息

        data_file = open('data.txt', 'a+')
        data_file.write("\n")                                   # 打开文件后首先在最后文件末尾换行
        data_file.write(imput_list_str)
        data_file.close()

        print("插入1条新增语句")


# 删除函数方法
def remove():
    data_value = table_info()
    input_remove = input('请输入删除语句：')
    id_value = input_remove[input_remove.rfind('=', 1) + 2:]                # 截取ID值

    if input_remove[:32] == ("del from staff_table where id = "):
        data_file1 = open('data1.txt', 'a+', encoding='utf-8')
        id_value_1 = (int(id_value) - 1)                                    # id值减一，因为删除数组下标值是从零开始
        del data_value[id_value_1]

        for i in data_value:
            str_i = ','.join(i).replace("\n","")
            data_file1.write(str_i)
            data_file1.write("\n")

        data_file1.flush()
        data_file1.close()

        os.remove("data.txt")                                               # 将原文件删除
        os.rename("data1.txt","data.txt")                                   # 将新文件更名为原文件名称

        print("删除1条数据")

    else:
        print("您输入的格式不正确！")


# 修改函数方法
def update():
    data_value = table_info()

    input_update = input('请输入修改语句：')
    if input_update[:22] == "UPDATE staff_table SET":
        num1 = input_update[:35][29:]                               # 截取dept="Market"
        num2 = input_update[:29][27:]                               # 截取age=25

        data_file1 = open('data1.txt', 'a+', encoding='utf-8')
        if input_update[:28] == "UPDATE staff_table SET dept=":
            count = 0
            for i in data_value:
                if i[4] == 'IT':
                    i[4] = num1
                    count += 1

            for i in data_value:
                str_i = ','.join(i).replace("\n", "")
                data_file1.write(str_i)
                data_file1.write("\n")

            data_file1.flush()
            data_file1.close()

            os.remove("data.txt")
            os.rename("data1.txt", "data.txt")

            print("所修改了%d条数据" % count)

        elif input_update[:27] == "UPDATE staff_table SET age=":
            count = 0
            for i in data_value:
                if i[1] == 'Alex Li':
                    i[2] = num2
                    count += 1

            for i in data_value:
                str_i = ','.join(i).replace("\n", "")
                data_file1.write(str_i)
                data_file1.write("\n")

            data_file1.flush()
            data_file1.close()

            os.remove("data.txt")
            os.rename("data1.txt", "data.txt")

            print("所修改了%d条数据" % count)
        else:
            print("您输入的格式不正确！")

    else:
        print("您输入的格式不正确！")


while True:

    print('''
***************************欢迎进入员工信息增删改查程序***************************
    1. 模糊查询  (语法： find name,age from staff_table where age > 22 
                       find * from staff_table where dept = "IT"
                       find * from staff_table where enroll_date like "2013" )
                       
    2. 新增信息  (语法： add staff_table Alex,25,134435344,IT,2015-10-29 )
    
    3. 删除信息  (语法： del from staff_table where id = 3)
    
    4. 修改信息  (语法： UPDATE staff_table SET dept="Market" WHERE dept = "IT"
                       UPDATE staff_table SET age=25 WHERE name = "Alex Li" )
******************************************************************************
    ''')

    choice = int(input('请选择要进入的功能：'))
    if choice == 1:
        print("-------成功进入查询功能-------")
        query()
        break

    elif choice == 2:
        print("-------成功进入新增功能-------")
        add()
        break

    elif choice == 3:
        print("-------成功进入删除功能-------")
        remove()
        break

    elif choice == 4:
        print("-------成功进入修改功能-------")
        update()
        break

    else:
        print("输入的信息有误！")
