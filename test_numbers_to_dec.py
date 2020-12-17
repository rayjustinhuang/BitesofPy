import pytest

from numbers_to_dec import list_to_decimal

def check_nonint():
    with pytest.raises(TypeError):
        list_to_decimal([1, 2, True])
    with pytest.raises(TypeError):
        list_to_decimal([1, 2, '5'])
    with pytest.raises(TypeError):
        list_to_decimal([1, 2.4, 8])
    
        
def check_outofrange():
    with pytest.raises(ValueError):
        list_to_decimal([-3, 5, 9])
        
    with pytest.raises(ValueError):
        list_to_decimal([11, 1, 2])
        