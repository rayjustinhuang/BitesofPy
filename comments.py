import re

def strip_comments(code):
    # see Bite description
    triple_quotes = re.compile(r'[\s]{4}"""[\S\s]*?"""\n')
    single_comments = re.compile(r"[\s]{4}#\s.+\n")
    inline_comments = re.compile(r'^\s{2}#\s[\S\s]+')
    
    no_comments = re.sub(single_comments, "", code)
    no_inlines = re.sub(inline_comments, "", no_comments)
    no_multiline_strings = re.sub(triple_quotes, "", no_inlines)
    
    return no_multiline_strings
    pass

code = '''
def say_hello(name):
    """A simple function that says hello... Richie style"""
    print(f"Hello {name}, is it me you're looking for?")
'''
single_docstring_after_strip = '''
def say_hello(name):
    print(f"Hello {name}, is it me you're looking for?")
'''

#print(strip_comments(code))
#assert strip_comments(code) == single_docstring_after_strip