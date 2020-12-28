from fizzbuzz import fizzbuzz

# write one or more pytest functions below, they need to start with test_
def test_normalcases():
    assert fizzbuzz(15) == 'Fizz Buzz'
    assert fizzbuzz(6) == 'Fizz'
    assert fizzbuzz(40) == 'Buzz'
    
def test_numbercases():
    assert fizzbuzz(13) == 13
    assert fizzbuzz(1) == 1
    assert fizzbuzz(14) == 14