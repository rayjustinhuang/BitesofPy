import re


def count_n_repetitions(text, n=1):
    """
    Counts how often characters are followed by themselves for
    n times.

    text: UTF-8 compliant input text
    n: How often character should be repeated, defaults to 1
    """
    findall_list = re.findall(rf'([\s\S])(?=\1{{{n}}})', text)
    
    return len(findall_list)
    
#print(count_n_repetitions("????{{{?}}}", 1))

def count_n_reps_or_n_chars_following(text, n=1, char=""):
    """
    Counts how often characters are repeated for n times, or
    followed by char n times.

    text: UTF-8 compliant input text
    n: How often character should be repeated, defaults to 1
    char: Character which also counts if repeated n times
    """
    
    if char == "":
        
        findall_n_reps = re.findall(rf'([\s\S])(?=\1{{{n}}})', text)
        
        return len(findall_n_reps)
        
    else:
        
        if char in '<([{\\^-=$!|]})?*+.>':
            char = f'\\{char}'
        
        print(char)
    
        findall_n_chars_following = re.findall(rf'([\s\S])(?=\1{{{n}}})|([\s\S])(?={char}{{{n}}})', text)
        
        print(findall_n_chars_following)
    
        return len(findall_n_chars_following)

def check_surrounding_chars(text, surrounding_chars):
    """
    Count the number of times a character is surrounded by
    characters from the surrounding_chars list.

    text: UTF-8 compliant input text
    surrounding_chars: List of characters
    """
    corrected_chars = []
    
    for char in surrounding_chars:
        if char in '<([{\\^-=$!|]})?*+.>':
            corrected_chars.append(f'\\{char}')
        else:
            corrected_chars.append(char)
            
    check_surrounding = re.findall(rf'(?<=[{"".join(corrected_chars)}])([\s\S])(?=[{"".join(corrected_chars)}])', text)
        
    return len(check_surrounding)
    