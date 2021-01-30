def dec_to_base(number, base):
    """
    Input: number is the number to be converted
           base is the new base  (eg. 2, 6, or 8)
    Output: the converted number in the new base without the prefix (eg. '0b')
    """
    # your code
    new_number = ""
    quotient = number % base
    
    if quotient < base:
        new_number += str(quotient)
    else:
        new_number += str(quotient)
        dec_to_base(quotient, base)
        
    return int(new_number)
    # return n
    

#dec_to_base(256, 8)