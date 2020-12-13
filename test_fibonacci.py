from fibonacci import fib

# write one or more pytest functions below, they need to start with test_
def negative_number(n):
    assert n > 0
    
def check_result(n):
    if n == 0:
        assert n == 0
    elif n == 1:
        assert n == 1
    else:
        pass
	#assert