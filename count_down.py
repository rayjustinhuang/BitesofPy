from functools import singledispatch


@singledispatch
def count_down(data_type):
    # TODO: Learn how to use singledispatch!
    count = len(data_type)
    
    while count != 0:
        print(data_type[:count])
        count -= 1
    pass

@count_down.register
def _(arg: int):
    count_down(str(arg))
    
@count_down.register
def _(arg: tuple):
    count_down(''.join(str(i) for i in arg))
    
@count_down.register
def _(arg: list):
    count_down(''.join(str(i) for i in arg))
    
@count_down.register
def _(arg: set):
    count_down(''.join(str(i) for i in arg))