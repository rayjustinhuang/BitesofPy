def sort_words_case_insensitively(words):
    """Sort the provided word list ignoring case, and numbers last
       (1995, 19ab = numbers / Happy, happy4you = strings, hence for
        numbers you only need to check the first char of the word)
    """
    key = lambda text: 'z'+text if text[0].isdigit() else text.lower()
    return sorted(words, key=key)
    pass