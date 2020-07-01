from functools import wraps


def int_args(func):
    @wraps(func)
    # complete this decorator
    def checker(*args):
        inputs = [*args]
        
        for i in inputs:
            if type(i) != int:
                raise TypeError
            elif i < 0:
                raise ValueError
        
        func(*args)
    return int_args
    