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
    
        findall_n_chars_following = re.findall(rf'([\s\S])(?=\1{{{n}}})|([\s\S])(?={char}{{{n}}})', text)
        
        print(findall_n_chars_following)
    
        return len(findall_n_chars_following)
    
#findall_n_reps) + len(findall_n_chars_following)
print(count_n_reps_or_n_chars_following("????{{{?}}}", 1, 'z'))
print(count_n_reps_or_n_chars_following("zz Don't count double!", 1, 'z'))


def check_surrounding_chars(text, surrounding_chars):
    """
    Count the number of times a character is surrounded by
    characters from the surrounding_chars list.

    text: UTF-8 compliant input text
    surrounding_chars: List of characters
    """
    count = 0
    for char in surrounding_chars:
        count += len(re.findall(rf'([\s\S])(?={{char}})', text))
        count += len(re.findall(rf'([\s\S])(?<={{char}})', text))
        
    return count
        