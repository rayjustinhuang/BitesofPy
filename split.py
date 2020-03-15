import re

def get_sentences(text):
    """Return a list of sentences as extracted from the text passed in.
       A sentence starts with [A-Z] and ends with [.?!]"""
    sentence = re.compile(r'[A-Z][^.]+[.?!]')
    
    sentence_list = re.findall(sentence, text)
    
    return sentence_list
    pass

text = """
PyBites was founded 19th of December 2016. That means that today,
14th of October 2019 we are 1029 days old. Time flies when you code
in Python. Anyways, good luck with this Bite. What is your favorite editor?
""" 

print(get_sentences(text))