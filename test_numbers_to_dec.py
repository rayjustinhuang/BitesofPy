import pytest

from numbers_to_dec import list_to_decimal

def check_nonnumber():
    with pytest.raises(TypeError):
        list_to_decimal([1, 2, True])
        
def check_negatives():
    with pytest.raises(ValueError):
        list_to_decimal([-3, 5, 9])