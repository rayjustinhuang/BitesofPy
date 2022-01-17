from collections import OrderedDict

def romanize(decimal_number):
    """Takes a decimal number int and converts its Roman Numeral str"""
    answer = ''
    running_figure = decimal_number
    
    if type(decimal_number) != int:
        raise ValueError
    
    if decimal_number <= 0 or decimal_number >= 4000:
        raise ValueError
        
    roman = OrderedDict()
    roman[1000] = "M"
    roman[900] = "CM"
    roman[500] = "D"
    roman[400] = "CD"
    roman[100] = "C"
    roman[90] = "XC"
    roman[50] = "L"
    roman[40] = "XL"
    roman[10] = "X"
    roman[9] = "IX"
    roman[5] = "V"
    roman[4] = "IV"
    roman[1] = "I"
    
    for key in roman.keys():
        count = running_figure // key
        answer += roman[key] * count
        running_figure -= key * count
        
    return answer
    
    pass