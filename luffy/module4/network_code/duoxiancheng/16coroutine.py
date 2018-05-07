
# 单纯地切换反而会降低运行效率
# 串行执行
# import time
# def consumer(res):
#     '''任务1:接收数据,处理数据'''
#     pass
#
# def producer():
#     '''任务2:生产数据'''
#     res = []
#     for i in range(10000000):
#         res.append(i)
#
#     return res
#
# start = time.time()
#
# #串行执行
# res = producer()
# consumer(res)
# stop = time.time()
# print(stop - start)


# 基于yield并发执行
''''''
# import time
# def consumer():
#     '''任务1：接收数据,处理数据'''
#     while True:
#         x = yield
#
# def producer():
#     '''任务2：生产数据'''
#     g = consumer()
#     next(g)
#     for i in range(10000000):
#         g.send(i)
#
# start = time.time()
#
# # 基于yield保持状态，实现两个任务直接来回切换，既并发的效果
# # 如果每个任务中都加上打印，那么明显地看到两个任务的打印是你一次我一次，即并发执行的
# producer()
# stop = time.time()
#
# print(stop - start)

# 并发执行
'''
import time
def producer():
    g = consumer()
    next(g)
    for i in range(10000000):
        g.send(i)

def consumer():
    while True:
        res = yield

start_time = time.time()
producer()
stop_time = time.time()
print(stop_time - start_time)
'''

# 串行执行
import time
def producer():
    res = []
    for i in range(10000000):
        res.append(i)
    return res

def consumer(res):
    pass

start_time = time.time()
res = producer()
consumer(res)
stop_time = time.time()
print(stop_time - start_time)
