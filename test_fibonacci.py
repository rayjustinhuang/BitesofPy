from fibonacci import fib
import pytest

# write one or more pytest functions below, they need to start with test_
def test_negative_number():
    with pytest.raises(ValueError):
        fib(-1)
    
def test_check_result():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(11) == 89