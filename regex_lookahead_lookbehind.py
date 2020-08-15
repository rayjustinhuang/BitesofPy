import re


def count_n_repetitions(text, n=1):
    """
    Counts how often characters are followed by themselves for
    n times.

    text: UTF-8 compliant input text
    n: How often character should be repeated, defaults to 1
    """
    findall_list = re.findall(rf'([\s\S]+)\1{{{n},}}', text)
    
    return len(findall_list)
    
print(count_n_repetitions("\n\n\nAs are newlines\n\n\n", 2))

def count_n_reps_or_n_chars_following(text, n=1, char=""):
    """
    Counts how often characters are repeated for n times, or
    followed by char n times.

    text: UTF-8 compliant input text
    n: How often character should be repeated, defaults to 1
    char: Character which also counts if repeated n times
    """
    findall_n_reps = re.findall(rf'(.)(?={n})', text)
    findall_n_chars_following = re.findall(rf'(.)(?={char})', text)
    
    return len(findall_n_reps) + len(findall_n_chars_following)
    
#print(count_n_reps_or_n_chars_following("1112345", 2, 'z'))


def check_surrounding_chars(text, surrounding_chars):
    """
    Count the number of times a character is surrounded by
    characters from the surrounding_chars list.

    text: UTF-8 compliant input text
    surrounding_chars: List of characters
    """
    count = 0
    for char in surrounding_chars:
        count += len(re.findall(rf'(.)(?={char})', text))
        count += len(re.findall(rf'(.)(?<={char})', text))
        
    return count
        