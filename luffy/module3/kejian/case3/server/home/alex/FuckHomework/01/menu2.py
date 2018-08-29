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

current_layers = dic # dic["山西"]
# layers = [dic, dic]
layers = [dic]

while True:
    for i in current_layers:
        print(i)
    choice = input(">>:").strip()  # 用户输入选项
    # 判断输入是否有效
    if choice in current_layers:
         layers.append(current_layers)  # 把当前层菜单添加到全部层，用于返回上一级使用
         current_layers = current_layers[choice]  # 把当前层换成新的
    elif choice.upper() == "B":
        current_layers = layers[-1]
        layers.pop()







