import os
import urllib.request

# PREWORK
DICTIONARY = os.path.join('/tmp', 'dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)
scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}


# start coding

def load_words():
    """Load the words dictionary (DICTIONARY constant) into a list and return it"""
    with open(DICTIONARY,'r') as f:
        WordList = f.read().splitlines()
    return WordList
    pass

# print(load_words()[:10])

def calc_word_value(word):
    """Given a word calculate its value using the LETTER_SCORES dict"""
    return sum([LETTER_SCORES[letter] for letter in word.upper()])
    pass

# print(calc_word_value('aalii'))

def max_word_value(words):
    """Given a list of words calculate the word with the maximum value and return it"""
    word_values = dict(zip(words,[calc_word_value(word) for word in words]))
    return max(word_values, key=word_values.get)
    pass

# max_word_value(['ate','apple','qi'])