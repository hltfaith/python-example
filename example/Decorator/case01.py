
def outer(func):
    def inner(*args, **kwargs):
        print(inner.__doc__)
        return func()

    return inner

@outer
def function():

    '''
    hello,function interface
    :return:
    '''

    print("func")

function()



