
# 有三种不同的队列用法
# 队列：先进先出
'''
import queue
q = queue.Queue()
q.put('first')
q.put('second')
q.put('third')

print(q.get())
print(q.get())
print(q.get())

'''

# 堆栈：最后进的先出
'''
import queue
q = queue.LifoQueue()
q.put('first')
q.put('second')
q.put('third')

print(q.get())
print(q.get())
print(q.get())

'''

# 优先级队列：存储数据时可设置优先级的队列
'''
import queue

q = queue.PriorityQueue()
q.put((20, 'a')) # put进入一个元组，元组的第一个元素是优先级(通常是数字，也可以是非数字之间的比较),数字越小优先级越高
q.put((10, 'b'))
q.put((30, 'c'))

print(q.get())
print(q.get())
print(q.get())
'''


# 结果(数字越小优先级越高,优先级高的优先出队)
