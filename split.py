import re

def get_sentences(text):
    """Return a list of sentences as extracted from the text passed in.
       A sentence starts with [A-Z] and ends with [.?!]"""
    sentence = re.compile(r'(\s*[!?.])\s([A-Z])')
    
    lines = re.split(sentence, text)
    
    lines.insert(0, "")
    
    sentence_list = ["".join(lines[n:n+3]) for n in range(0,len(lines),3)]
    
    final_list = []
    for sentence in sentence_list:
        final_list.append(re.sub('\n', ' ', sentence).strip())
    
    return final_list
    pass