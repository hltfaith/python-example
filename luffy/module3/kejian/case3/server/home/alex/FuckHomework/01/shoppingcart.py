"""
购物车
功能要求：

要求用户输入总资产，例如：2000
显示商品列表，让用户根据序号选择商品，加入购物车
购买，如果商品总额大于总资产，提示账户余额不足，否则，购买成功。
附加：可充值、某商品移除购物车
goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]
"""

# 要求用户输入总资产，例如：2000
asset = input("请输入总资产：").strip()
asset = int(asset)

# 显示商品列表，让用户根据序号选择商品，加入购物车
# 显示商品列表

goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]

# 索引序号 方法一
# for i in range(len(goods)):
#     print(i, goods[i])

# 索引序号 方法二
for i in goods:
    print(goods.index(i)+1, i)
# 让用户根据序号选择商品，加入购物车
shopping_cart = []

while True:
    choice = input("商品序号：").strip()
    if choice.upper() == "C":  # 准备结账
        # 购买，如果商品总额大于总资产，提示账户余额不足，否则，购买成功。
        # 要求商品总额
        money = 0
        # shopping_cart[0]['price']  # 取出第一个商品的价格
        # shopping_cart[1]['price']  # 取出第二个商品的价格
        for t in shopping_cart:
            money += t['price']
        if money > asset:
            print("账户余额不足")
        else:
            print("购买成功")
            break
    # 这里需要判断 是不是 数字 isdigit()
    # 是不是有效的数字  0 <=  < len(goods)
    else:
        choice = int(choice) # 转成int类型
        sp = goods[choice]  # 取到具体的商品
        shopping_cart.append(sp)  # 添加到购物车
        print(sp, "现已加入豪华午餐。")
        print(shopping_cart)




"""

shopping_cart = [
    {
        'name': '电脑',
        'price': 1999
    },
    {
        'name': '美女',
        'price': 998
    }
]
"""















