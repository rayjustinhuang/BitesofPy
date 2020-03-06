import re

def strip_comments(code):
    # see Bite description
    three_indent_docstrings = re.compile(r'[\s]{12}"""[\S\s]*?"""\n')
    class_docstrings = re.compile(r'[\s]{8}"""[\S\s]*?"""\n')
    triple_quotes = re.compile(r'[\s]{4}"""[\S\s]*?"""\n')
    multiline_quotes = re.compile(r'"""[\S\s]*?"""\n')
    single_comments = re.compile(r"[\s]{4}#\s.+\n")
    inline_comments = re.compile(r'\s{2}#\s[\S\s]+\n')
    basic_comments = re.compile(r'#\s[\S\s]*?\n')
    
    no_three_indents = re.sub(three_indent_docstrings, "", code)
    no_docstrings = re.sub(class_docstrings, "", no_three_indents)
    no_comments = re.sub(single_comments, "", no_docstrings)
    no_inlines = re.sub(inline_comments, "", no_comments)
    no_triple_quotes = re.sub(triple_quotes, "", no_inlines)
    no_basic_comments = re.sub(basic_comments, "", no_triple_quotes)
    no_multiline_strings = re.sub(multiline_quotes, "", no_basic_comments)
    
    return no_multiline_strings
    pass