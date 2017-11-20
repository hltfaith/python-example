# -*- coding: utf-8 -*-
# Version: 3.6.1
#  Author: Wu changhao

# 二、 购物车程序：

# 功能要求：
# 1. 启动程序后，输入用户名密码后，让用户输入工资，然后打印商品列表
# 2. 允许用户根据商品编号购买商品
# 3. 用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
# 4. 可随时退出，退出时，打印已购买商品和余额
# 5. 在用户使用过程中，关键输出，如余额，商品加入购物车等消息，需高亮显示

goods = [
{"name": "电脑", "price": 1999},
{"name": "鼠标", "price": 10},
{"name": "游艇", "price": 20},
{"name": "美女", "price": 998}
]

userlist = {"xiaohong": "0", "xiaoming": "1", "xiaojun": "2"}
surplus = 0

while True:
    username = input("请输入您的用户名 :")
    password = input("请输入您的密码 :")
    if username in userlist and password in userlist.values():
        wages = int(input("欢迎登陆购物车系统，请输入您的工资："))
        while True:
            count = 0
            print("商品名称"+"  "+"单价")
            for i in goods:
                print(str(count)+"."+list(i.values())[0]+"   "+str(list(i.values())[1]))
                count += 1
            buy_num = input("请选择要购买的商品编号(退出输入q)：")
            if buy_num == 'q' or buy_num == 'Q':
                print("购物车系统已成功退出！")
                exit()
            elif int(buy_num) <= 3:
                commodity = list(goods[int(buy_num)].values())[0]
                if wages == wages and surplus == 0:
                    surplus = (wages - list(goods[int(buy_num)].values())[1])
                    print("请您好您已成功购买%s商品，所剩余额%s元。" % (commodity, surplus))
                    continue

                elif surplus < list(goods[int(buy_num)].values())[1]:
                    print("您的余额不足，无法购买此商品。请查看其他商品：")
                    continue

                elif wages != surplus:
                    surplus = (surplus - list(goods[int(buy_num)].values())[1])
                    print("请您好您已成功购买%s商品，所剩余额%s元。(退出输入q)" % (commodity, surplus))
                    continue

            else:
                print("您所输入的信息有误，请重新输入！")
                continue
    else:
        print("对不起，您的用户名或密码有误，请重新输入！(退出输入q)")