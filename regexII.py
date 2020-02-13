import re


def has_timestamp(text):
    """Return True if text has a timestamp of this format:
       2014-07-03T23:30:37"""
    pattern = r'[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}'
    find = re.findall(pattern, text)
    return bool(find)
    pass


def is_integer(number):
    """Return True if number is an integer"""
    pattern = r'^[-+]?[\d]+$'
    return re.search(pattern, number)
    pass


def has_word_with_dashes(text):
    """Returns True if text has one or more words with dashes"""
    pattern = r'[0-9a-zA-Z]+-[0-9a-zA-Z]+'
    return re.search(pattern, text)
    pass


def remove_all_parenthesis_words(text):
    """Return text but without any words or phrases in parenthesis:
       'Good morning (afternoon)' -> 'Good morning' (so don't forget
       leading spaces)"""
    pattern = r'[\(][0-9a-zA-Z]+[\)]'
    return re.sub(pattern, "", text).strip()
    pass


def split_string_on_punctuation(text):
    """Split on ?!.,; - e.g. "hi, how are you doing? blabla" ->
       ['hi', 'how are you doing', 'blabla']
       (make sure you strip trailing spaces)"""
    pass


def remove_duplicate_spacing(text):
    """Replace multiple spaces by one space"""
    pass


def has_three_consecutive_vowels(word):
    """Returns True if word has at least 3 consecutive vowels"""
    pass


def convert_emea_date_to_amer_date(date):
    """Convert dd/mm/yyyy (EMEA date format) to mm/dd/yyyy
       (AMER date format)"""
    pass