def is_armstrong(n: int) -> bool:
    
    string_n = str(n)
    
    power = len(string_n)
    
    compare = 0
    
    for i in string_n:
        compare += int(i)**power
        
    return n == compare
    # you code