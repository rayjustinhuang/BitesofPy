import os
import urllib.request
from collections import Counter

# data provided
stopwords_file = os.path.join('/tmp', 'stopwords')
harry_text = os.path.join('/tmp', 'harry')
urllib.request.urlretrieve('http://bit.ly/2EuvyHB', stopwords_file)
urllib.request.urlretrieve('http://bit.ly/2C6RzuR', harry_text)

def strip_nonalnum(word):
    correct_chars = [ch for ch in word if ch.isalpha() or ch.isnumeric()]
    return "".join(correct_chars)

def get_harry_most_common_word():
    with open(harry_text) as f:
        with open(stopwords_file) as stopwords:
            stopwords_list = stopwords.read().split()
            words = [strip_nonalnum(word).lower() for word in f.read().split() if strip_nonalnum(word).lower() not in stopwords_list and not strip_nonalnum(word).lower()]
    word_count = Counter(words)
    return word_count.most_common()[:10]
    pass

print(get_harry_most_common_word())