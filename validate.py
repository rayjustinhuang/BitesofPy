from functools import wraps


def int_args(func):
    @wraps(func)
    # complete this decorator
    def checker(*args):
        
        for i in args:
            if type(i) != int:
                raise TypeError
            elif i < 0:
                raise ValueError
        
        return func(*args)
    return checker