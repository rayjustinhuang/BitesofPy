import string
VOWELS = 'aeiou'
PYTHON = 'python'


def contains_only_vowels(input_str):
    """Receives input string and checks if all chars are
       VOWELS. Match is case insensitive."""
    return all(i.lower() in VOWELS for i in input_str)
    pass


def contains_any_py_chars(input_str):
    """Receives input string and checks if any of the PYTHON
       chars are in it. Match is case insensitive."""
    return any(i.lower() in PYTHON for i in input_str)
    pass


def contains_digits(input_str):
    """Receives input string and checks if it contains
       one or more digits."""
    return any(i in string.digits for i in input_str)
    pass