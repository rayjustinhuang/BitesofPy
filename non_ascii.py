def extract_non_ascii_words(text):
    """Filter a text returning a list of non-ascii words"""
    word_list = text.split()
    ascii_chars = [chr(i) for in in range(128)]
    result = []
    
    for word in word_list:
        if word.intersection(ascii_chars) != set(list(word)):
            result.append(word)
            
    return result
    pass