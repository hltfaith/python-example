# -*- coding: utf-8 -*-
# Version: 3.6.1
#  Author: Wu changhao

# 需求：
#   可依次选择进入各子菜单
#   可从任意一层往回退到上一层
#   可从任意一层退出程序


menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {}
            },
            '上地': {
                '百度': {}
            }
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {}
        },
        '朝阳': {},
        '东城': {}
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车站': {
                '携程': {}
            }
        },
        '浦东': {}
    },
    '山东': {}
}



while True:
    for i in list(menu):
        print(i)
    choice = input("请选择要进入的城市，退出程序请输入q：")  # 北京
    if choice in list(menu):

        while True:
            print('所在的城市: %s，返回上一级请输入b' % choice)
            for i in list(menu[choice]):
                print(i)
            choice1 = input("请选择要进入的地区，退出程序请输入q：")  # 海淀
            if choice1 in list(menu[choice]):

                while True:
                    print('所在的城市: %s，返回上一级请输入b' % choice1)
                    for i in list(menu[choice][choice1]):
                        print(i)
                    choice2 = input("请选择要进入的街道，退出程序请输入q：")  # 五道口
                    if choice2 in list(menu[choice][choice1]):

                        while True:
                            print('所在的城市: %s，返回上一级请输入b' % choice2)
                            for i in list(menu[choice][choice1][choice2]):
                                print(i)
                            choice3 = input("请选择要进入的地方，退出程序请输入q：")  # soho
                            if choice3 in list(menu[choice][choice1][choice2]):

                                while True:
                                    print('所在的城市: %s，返回上一级请输入b' % choice2)
                                    print('已是最后一级菜单请返回上一级目录。')
                                    choice4 = input("请选择要进入的地方，退出程序请输入q：")  # end
                                    if choice4 == 'b':
                                        break
                                    elif choice4 == 'q' or choice == 'Q':
                                        print("程序退出成功！")
                                        exit()
                                    else:
                                        print("所输入的字符有误，请重新输入！")
                                        continue

                            elif choice3 == 'b':
                                break
                            elif choice3 == 'q' or choice3 == 'Q':
                                print("程序退出成功！")
                                exit()
                            else:
                                print("所输入的字符有误，请重新输入！")
                                continue

                    elif choice2 == 'b':
                        break
                    elif choice2 == 'q' or choice2 == 'Q':
                        print("程序退出成功！")
                        exit()
                    else:
                        print("所输入的字符有误，请重新输入！")
                        continue

            elif choice1 == 'b':
                break
            elif choice1 == 'q' or choice1 == 'Q':
                print("程序退出成功！")
                exit()
            else:
                print("所输入的字符有误，请重新输入！")
                continue

    elif choice == 'q' or choice == 'Q':
        print("程序退出成功！")
        exit()
    else:
        print("所输入的字符有误，请重新输入！")
        continue
