import re

def get_sentences(text):
    """Return a list of sentences as extracted from the text passed in.
       A sentence starts with [A-Z] and ends with [.?!]"""
    sentence = re.compile(r'[A-Z][^.]+[.?!][^A-Z)]*')
    
    sentence_list = re.findall(sentence, text)
    
    final_list = []
    for sentence in sentence_list:
        final_list.append(re.sub('\n', ' ', sentence))
    
    return final_list
    pass

text = """
We are looking forward attending the next Pycon in the U.S.A.
in 2020. Hope you do so too. There is no better Python networking
event than Pycon. Meet awesome people and get inspired. Btw this
dot (.) should not end this sentence, the next one should. Have fun!
"""

print(get_sentences(text))