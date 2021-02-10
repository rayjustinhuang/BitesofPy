def tail(filepath, n):
    """Similate Unix' tail -n, read in filepath, parse it into a list,
       strip newlines and return a list of the last n lines"""
       
    with open(filepath) as f:
        text = f.read()
        lines = text.splitlines()
        max_n = len(lines)
        
        print(lines)
    
    if n > max_n:
        return lines
    else:
        return lines[max_n-n:]
    pass