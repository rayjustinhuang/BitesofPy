import itertools
import os
import urllib.request

# PREWORK
TMP = os.getenv("TMP", "/tmp")
DICT = 'dictionary.txt'
DICTIONARY = os.path.join(TMP, DICT)
urllib.request.urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{DICT}',
    DICTIONARY
)

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])


def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    
    return ["".join(word).lower() for word in _get_permutations_draw(draw) if "".join(word).lower() in dictionary]
    pass

def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
       
    letters = [i.strip() for i in draw.split(',')]
    
    all_perms = []
    
    for i in range(2,len(draw)):
        all_perms += itertools.permutations(letters, i)
        
    return all_perms
    pass

#draw = 'T, I, I, G, T, T, L'

#print(get_possible_dict_words(draw))

#print(["".join(word) for word in _get_permutations_draw(draw)])