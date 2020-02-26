def strip_comments(code):
    # see Bite description
    triple_quotes = re.compile(r'"""[.]+"""')
    single_comments = re.compile(r'#\s')
    inline comments = re.compile(r'^\s{2}#\s\\n$')
    pass