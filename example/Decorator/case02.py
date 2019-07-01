import functools

def outter(func):

    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(inner.__doc__)
        return func()

    return inner

@outter
def function():

    """
    hello
    :return:
    """
    print("func")
    
function()

