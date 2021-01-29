def dec_to_base(number, base):
    """
    Input: number is the number to be converted
           base is the new base  (eg. 2, 6, or 8)
    Output: the converted number in the new base without the prefix (eg. '0b')
    """
    # your code
    new_number = ""
    
    if quotient < base:
        new_number += str(quotient)
    else:
        quotient = number % base
        new_number += str(quotient)
        dec_to_base(quotient, base)
        
    return int(new_number)
    # return n