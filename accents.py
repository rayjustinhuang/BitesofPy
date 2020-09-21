import unicodedata

def filter_accents(text):
    """Return a sequence of accented characters found in
       the passed in lowercased text string
    """
    accented_chars = set()
    
    for i in text:
        if unicodedata.decomposition(i) != "":
            accented_chars.add(i.lower())
            
    return sorted(list(accented_chars))
    pass