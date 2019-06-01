
# 过滤列表中所有奇数

def is_odd(n):
    return n % 2 == 1

newlist = list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(newlist)

