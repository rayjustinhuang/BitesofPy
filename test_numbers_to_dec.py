import pytest

from numbers_to_dec import list_to_decimal

def test_check_nonint():
    with pytest.raises(TypeError):
        list_to_decimal([1, 2, True])
    with pytest.raises(TypeError):
        list_to_decimal([1, 2, '5'])
    with pytest.raises(TypeError):
        list_to_decimal([1, 2.4, 8])
    
        
def test_check_outofrange():
    with pytest.raises(ValueError):
        list_to_decimal([-3, 5, 9])
    with pytest.raises(ValueError):
        list_to_decimal([11, 1, 2])
        
def test_check_goodexamples():
    assert list_to_decimal([4, 2, 6]) == 426
    assert list_to_decimal([0, 5, 1, 6, 9, 8]) == 51698
    assert list_to_decimal([3, 7]) == 37
    assert list_to_decimal([7]) == 7
        