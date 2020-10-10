from collections import Counter

def calculate_gc_content(sequence):
    """
    Receives a DNA sequence (A, G, C, or T)
    Returns the percentage of GC content (rounded to the last two digits)
    """
    joined = "".join(sequence.lower())
    
    count = Counter(joined)
    
    print(count)
    
    return round((count['g'] + count['c']) / (count['g'] + count['c'] + count['t'] + count['a'])*100,2)
    pass