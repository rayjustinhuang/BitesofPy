import re

def strip_comments(code):
    # see Bite description
    triple_quotes = re.compile(r'"""[\S\s]*?"""')
    single_comments = re.compile(r'#\s.+')
    # inline comments = re.compile(r'^\s{2}#\s\\n$')
    
    no_comments = re.sub(single_comments, "", code)
    no_multiline_strings = re.sub(triple_quotes, "", no_comments)
    
    print(no_multiline_strings)
    pass

code = '''
"""this is
my awesome script
"""
# importing modules
import re

def hello(name):
    """my function docstring"""
    return f'hello {name}'  # my inline comment
'''

strip_comments(code)