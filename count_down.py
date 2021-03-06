from functools import singledispatch


@singledispatch
def count_down(data_type):
    # TODO: Learn how to use singledispatch!
    try:
        count = len(data_type)
        
        while count != 0:
            print(data_type[:count])
            count -= 1
    
    except:
        raise ValueError
    pass

@count_down.register
def _(arg: int):
    count_down(str(arg))
    
@count_down.register
def _(arg: float):
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
    
@count_down.register
def _(arg: dict):
    count_down(''.join(str(i) for i in arg.keys()))

@count_down.register
def _(arg: range):
    count_down(list(arg))

