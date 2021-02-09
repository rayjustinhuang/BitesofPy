def tail(filepath, n):
    """Similate Unix' tail -n, read in filepath, parse it into a list,
       strip newlines and return a list of the last n lines"""
       
    with open(filepath) as f:
        text = f.read()
        lines = text.splitlines()
        max_n = len(lines)
    
    if n == 1:
        return lines[-1]
    elif n > max_n:
        return lines
    else:
        return lines[-n]
    pass