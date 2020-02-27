import re

def strip_comments(code):
    # see Bite description
    triple_quotes = re.compile(r'""".+"""', re.DOTALL)
    single_comments = re.compile(r'#\s.+')
    # inline comments = re.compile(r'^\s{2}#\s\\n$')
    
    print(re.sub(single_comments, "", code))
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