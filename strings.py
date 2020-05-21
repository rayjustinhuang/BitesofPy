from typing import List


def common_words(sentence1: List[str], sentence2: List[str]) -> List[str]:
    """
    Input:  Two sentences - each is a  list of words in case insensitive ways.
    Output: those common words appearing in both sentences. Capital and lowercase 
            words are treated as the same word. 

            If there are duplicate words in the results, just choose one word. 
            Returned words should be sorted by word's length.
    """
    common = []
    
    lower_sentence1 = [word.lower() for word in sentence1]
    lower_sentence2 = [word.lower() for word in sentence2]
    
    for word in lower_sentence1:
        if word in lower_sentence2:
            common.append(word)
    
    return sorted(list(set(common)), key=len)
    pass