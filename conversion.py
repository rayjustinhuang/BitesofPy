def dec_to_base(number, base):
    """
    Input: number is the number to be converted
           base is the new base  (eg. 2, 6, or 8)
    Output: the converted number in the new base without the prefix (eg. '0b')
    """
    # your code
    if number == 0:
        return 0
    else:
        quotient = number % base
        return quotient + 10*dec_to_base(number//base, base)