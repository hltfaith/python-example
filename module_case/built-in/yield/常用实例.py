
'''

如何生成斐波那契數列
斐波那契（Fibonacci）數列是一个非常简单的递归数列，除第一个和第二个数外，任意一个数都可由前两个数相加得到。
用计算机程序输出斐波那契數列的前 N 个数是一个非常简单的问题，
许多初学者都可以轻易写出如下函数：

'''


'''
# 清单 1. 简单输出斐波那契數列前 N 个数
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1

fab(10)


结果没有问题，但有经验的开发者会指出，直接在 fab 函数中用 print 打印数字会导致该函数可复用性较差，
因为 fab 函数返回 None，其他函数无法获得该函数生成的数列。

'''

'''
# 清单 2. 输出斐波那契數列前 N 个数第二版
def fab(max):
    n, a, b = 0, 0, 1
    L = []

    while n < max:
        L.append(b)
        a, b = b, a + b
        n = n + 1

    return L

for n in fab(5):
    print(n)
'''


'''

利用 iterable 我们可以把 fab 函数改写为一个支持 iterable 的 class，以下是第三个版本的 Fab：
清单 4. 第三个版本



class Fab(object):
    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def next(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration()

# Fab 类通过 next() 不断返回数列的下一个数，内存占用始终为常数：
for n in Fab(5):
    print(n)


# 清单 5. 使用 yield 的第四版

def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

'''


'''

这段代码很短，但是诠释了yield关键字的核心用法，即逐个生成。在这里获取了两个生成器产生的值，即0和1。
分别由next函数和send()函数获得，这两个函数的区别我们后面会详细阐述。
关于__next__函数，这里先说明一下，我们可以利用__next__()这个函数持续获取符合fun函数规则的数，直到19结束。

生成器中最重要的函数是sent和__next__这两个函数，

sent函数
这里特别强调了sent函数，因为sent函数没有那么直观。__next__函数很好理解，
就是从上一个终止点开始，到下一个yield结束，返回值就是yield表达式的值。


第一次调用__next__函数的时候，我们从fun的起点开始，然后在yield处结束，需要注意的是，赋值语句不会调用，
此处yield i和含义和return差不多。

但是第二次调用__next__函数的时候，就会直接从上一个yield的结束处开始，也就是先执行赋值语句，然后输出字符串，
进入下一个循环，直到下一个yield或者生成器结束
再次看初始的那段代码，可以发现第二次调用的时候没有选择使用__next__函数，而是使用了一个sent()函数。

这里就需要注意，sent()函数的用法和__next__函数不太一样。sent()函数只能从yield之后开始，到下一个yield结束。
这也就意味着第一次调用必须使用__next__函数。
sent()函数最重要的作用在于它可以给yield对应的赋值语句赋值，比如上面那一段代码中的

如果调用__next()__函数，那么x=None。但是如果调用sent(5)，那么x=5。
除了上述将的两个特征以外，sent和next并没有什么区别，sent函数也会返回yield表达式对应的值

'''


def fun():
    for i in range(20):
        x = yield i
        print('good', x)


if __name__ == '__main__':
    a = fun()
    a.__next__()

    x = a.send(5)
    print(x)

