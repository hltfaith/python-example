# 文艺青年版三级菜单

"""
选做题：用户交互，显示省市县三级联动的选择

dic = {
    "河北": {
        "石家庄": ["鹿泉", "藁城", "元氏"],
        "邯郸": ["永年", "涉县", "磁县"],
    }
    "河南": {
        ...
    }
    "山西": {
        ...
    }
}
"""

dic = {
    "河北": {
        "石家庄": ["鹿泉", "藁城", "元氏"],
        "邯郸": ["永年", "涉县", "磁县"],
    },
    "河南": {
        "郑州": ["1", "2", "3"],
        "平顶山": ["4", "5", "6"]
    },
    "山西": {
        "A": ["11", "22", "33"],
        "C": ["44", "55", "66"]
    }
}

# 20行代码实现三级菜单

# lowB版三级菜单
# 如果输入的是b，就回到上一级
# 如果输入的是q，就退出

exit_flag = False

while not exit_flag:
    for i in dic:
        print(i)
    choice1 = input(">>:").strip()

    # 这是第一级，不能返回上级，只有一个Q退出
    if choice1.upper() == "Q":
        break


    kx = dic[choice1]  # 取到第二级的字典

    for j in kx:
        print(j)

    while not exit_flag:
        choice2 = input(">>:").strip()

        # 二级菜单有返回上级和退出
        if choice2.upper() == "Q":
            break
        if choice2.upper() == "B":
            exit_flag = True
            break


        zkx = kx[choice2]  # 取到第三级的字典


        for z in zkx:
            print(z)
        choice3 = input(">>:").strip()

        # 三级菜单也有返回上级和退出
        if choice3.upper() == "Q":
            exit_flag = True
            break
        if choice3.upper() == "B":
            continue
