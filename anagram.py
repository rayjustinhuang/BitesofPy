def is_anagram(word1, word2):
    """Receives two words and returns True/False (boolean) if word2 is
       an anagram of word1, ignore case and spacing.
       About anagrams: https://en.wikipedia.org/wiki/Anagram"""
       
    word1_list = [i for i in word1.lower() if i != " "]
    word2_list = [j for j in word2.lower() if j != " "]
    
    word1_list.sort()
    word2_list.sort()
    
    return word1_list == word2_list
    pass