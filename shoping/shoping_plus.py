# -*- coding: utf-8 -*-
# Version: 3.6.1
#  Author: Wu changhao
# Please Using username=changhao, password=null

# 二、 购物车程序：
# 功能需求：
# 1. 启动程序后，输入用户名密码后，让用户输入工资，然后打印商品列表
# 2. 允许用户根据商品编号购买商品
# 3. 用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
# 4. 可随时退出，退出时，打印已购买商品和余额
# 5. 在用户使用过程中，关键输出，如余额，商品加入购物车等消息，需高亮显示

# 扩展需求：
#   1. 用户下一次登陆后，输入用户名密码，直接回到上次的状态，即上次消费的余额什么的还是那些，再次登陆可继续购买
#   2. 允许查询之前的消费记录


goods = [
{"name": "电脑", "price": 1999},
{"name": "鼠标", "price": 10},
{"name": "游艇", "price": 20},
{"name": "美女", "price": 998}
]

surplus = 0        #定义剩余余额初始值为0

while True:
    print("---------------------------------------")
    print("-          欢迎您登陆购物车系统          -")
    print("---------------------------------------")
    username = input("请输入您的用户名 :")
    password = input("请输入您的密码 :")

    if username == "changhao" and password == "null":                                   #判断账户和密码是否正确
        user_check = open('shop_surplus.txt').read()                                    #打开商品余额文件，打开只读模式
        shop_surplus_length = len(user_check)                                           #定义变量，判断商品余额文件内容长度

        if shop_surplus_length == 0:                                                    #如果长度等于0时，表示用户为第一次进入购物车系统
            wages = int(input("欢迎登陆购物车系统，请输入您的工资："))                       #让用户输入自己的工资

        else:
            shop_surplus = open('shop_surplus.txt', 'r+', encoding='utf-8')             #打开商品余额文件，打开只读模式
            surplus = shop_surplus.readline()                                           #实例化商品余额文件
            print("欢迎您\033[1;31m%s\033[0m，再次登陆购物车系统!" % username)
            print("您的余额剩余\033[1;31m%s元\033[0m" % surplus)                          #检测用户显示上次购买商品的余额
            shop_surplus.close()

        while True:
            count = 0                                                                   #设置商品列表下标计数器，从0开始
            print("商品名称" + "  " + "单价")

            for i in goods:                                                             #遍历出商品的列表
                print(str(count) + "." + list(i.values())[0] + "   " + str(list(i.values())[1]))
                count += 1                                                              #每次循环商品列表下标加1

            buy_num = input("请选择要购买的商品编号(退出输入q)：")
            shop_add_text = open("shop_info.txt", "a", encoding='utf-8')                #打开商品信息文件，后续所购买的商品信息存在此文件

            if buy_num == 'q' or buy_num == 'Q':                                        #用户退出后，将所购买的商品列表和剩余余额信息显示
                print("购物车系统已成功退出！")
                print("----已购买的商品列表----")
                shop_info = open("shop_info.txt", "r+", encoding='utf-8')
                shop_name = shop_info.readline()
                shop_name_arr = shop_name.split(',')                                    #每次把购买的商品信息写入的格式如: "上海,"这种格式，所以在转换成数组是需要提前去除 ','
                shop_name_arr.pop()                                                     #转换过程中，数组最后一个信息是空值，需要每次把最后移除
                shop_name_list = set(shop_name_arr)
                for i in shop_name_list:                                                #遍历出商品中的数量
                    print(" %s*\033[1;31m%s\033[0m" % (i, shop_name_arr.count(i)))

                print("您所剩余额为\033[1;31m%s元 \033[0m " % surplus)
                shop_surplus = open('shop_surplus.txt', 'w')
                shop_surplus.write(str(surplus))                                        #每次退出程序，会将当前余额写入到商品余额文件中
                shop_surplus.close()
                print("----------------------")
                print("欢迎再次光临购物车系统!")
                exit()

            elif int(buy_num) <= 3:                                                     #如果用户输入的编号小于等于3，就进入以下内容
                commodity = list(goods[int(buy_num)].values())[0]                       #定义每次购买的商品名称

                if wages == wages and surplus == 0:                                     #如果第一次用户进入系统余额等于0时
                    surplus = (wages - list(goods[int(buy_num)].values())[1])           #工资减去商品等于余额
                    shop_add_text.write(list(goods[int(buy_num)].values())[0]+',')      #购买的商品信息，写入文件，格式为："电脑,"
                    shop_add_text.close()
                    print("您好,您已成功购买\033[1;31m%s\033[0m商品，所剩余额\033[1;31m%s元\033[0m。" % (commodity, surplus))
                    continue

                elif int(surplus) < int(list(goods[int(buy_num)].values())[1]):         #如果用户余额小于商品价格时
                    print("您的余额不足，无法购买此商品。请查看其他商品：")
                    continue

                elif wages != surplus:                                                  #如果工资不等余额时
                    surplus = (int(surplus) - list(goods[int(buy_num)].values())[1])    #余额减去商品价格等于余额
                    shop_add_text.write(list(goods[int(buy_num)].values())[0] + ',')    #购买的商品信息，写入文件，格式为："电脑,"
                    shop_add_text.close()
                    print("您好,您已成功购买\033[1;31m%s\033[0m商品，所剩余额\033[1;31m%s\033[0m元。(退出输入q)" % (commodity, surplus))
                    continue

            else:
                print("您所输入的信息有误，请重新输入！")
                continue

    else:
        print("对不起，您的用户名或密码有误，请重新输入！")