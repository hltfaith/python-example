
# 在序列中映射函数
counters = [1, 2, 3, 4]

def inc(x):
    return x + 10

print(list(map(inc, counters)))
# [11, 12, 13, 14]
