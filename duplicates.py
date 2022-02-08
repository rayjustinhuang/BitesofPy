def get_duplicate_indices(words):
    """Given a list of words, loop through the words and check for each
       word if it occurs more than once.
       If so return the index of its first occurrence.
       For example in the following list 'is' and 'it'
       occur more than once, and they are at indices 0 and 1 so you would
       return [0, 1]:
       ['is', 'it', 'true', 'or', 'is', 'it', 'not?'] => [0, 1]
       Make sure the returning list is unique and sorted in ascending order."""
       
    unique_words = set(words)
    indices = []  
     
    for word in unique_words:
        if words.count(word) > 1:
            indices.append(words.index(word))
            
    return indices
    pass