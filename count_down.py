from functools import singledispatch


@singledispatch
def count_down(data_type):
    # TODO: Learn how to use singledispatch!
    count = len(data_type)
    
    while count != 0:
        print(data_type[:count])
        count -= 1
    pass

@fun.register
def _(arg: int):
    count_down(str(arg))