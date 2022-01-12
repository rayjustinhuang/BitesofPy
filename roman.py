def romanize(decimal_number):
    """Takes a decimal number int and converts its Roman Numeral str"""
    answer = None
    
    if decimal_number <= 0 or decimal_number >= 4000:
        raise ValueError
    
    if (decimal_number // 1000) > 0:
        answer += 'M'*(decimal_number // 1000)
    pass