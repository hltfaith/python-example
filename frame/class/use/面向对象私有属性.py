
1. __dict__
class Person:
    静态变量 = 123
 
print(Person.__dict__) #内置的双下划线方法

执行输出：
{'__doc__': None, '静态变量': 123, '__module__': '__main__', '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__dict__': <attribute '__dict__' of 'Person' objects>}

总结：

引用静态变量
  1.类名.__dict__['静态变量名'] 可以查看，但是不能删改
  2.类名.静态变量名 直接就可以访问,可以删改
  删除一个静态变量 del 类名.静态变量名

2.


