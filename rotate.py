def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    length = len(string)
    
    if n == length:
        return string
    elif n > 0:
        return string[-(length-n):] + string[:n]
    else:
        return string[n:] + string[:length+n]
    pass