from multiprocessing import Queue


q=Queue(3)

q.put('hello')
q.put({'a':1})
q.put([3,3,3,])
print(q.full())

# q.put(4)

print(q.get())
print(q.get())
print(q.get())
print(q.empty())

print(q.get())