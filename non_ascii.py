def extract_non_ascii_words(text):
    """Filter a text returning a list of non-ascii words"""
    word_list = text.split()
    ascii_chars = set(chr(i) for i in range(128))
    result = []
    
    for word in word_list:
        if set(word).intersection(ascii_chars) != set(list(word)):
            result.append(word)
            
    return result
    pass