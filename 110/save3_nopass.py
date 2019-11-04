def divide_numbers(numerator, denominator):
    """For this exercise you can assume numerator and denominator are of type
       int/str/float.
       Try to convert numerator and denominator to int types, if that raises a
       ValueError reraise it. Following do the division and return the result.
       However if denominator is 0 catch the corresponding exception Python
       throws (cannot divide by 0), and return 0"""
    try:
        int(numerator)
    except ValueError:
        raise ValueError('The numerator cannot be made into an integer')
    
    top = int(numerator)
    
    try:
        int(denominator)
    except ValueError:
        raise ValueError('The denominator cannot be made into an integer')
    
    below = int(denominator)
    
    try:
        top/below
    except:
        return 0
    
    return top/below
    pass

print(divide_numbers(10,5))
print(divide_numbers('s',5))
print(divide_numbers('10',0))