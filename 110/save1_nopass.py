def divide_numbers(numerator, denominator):
    """For this exercise you can assume numerator and denominator are of type
       int/str/float.
       Try to convert numerator and denominator to int types, if that raises a
       ValueError reraise it. Following do the division and return the result.
       However if denominator is 0 catch the corresponding exception Python
       throws (cannot divide by 0), and return 0"""
    try:
        top = int(numerator)
    except ValueError:
        return ValueError('The numerator cannot be made into an integer')
    
    try:
        below = int(denominator)
    except ValueError:
        return ValueError('The denominator cannot be made into an integer')
        
    try:
        return top/bottom
    except:
        return 0
    pass

print(type(5) == int)