import re

def strip_comments(code):
    # see Bite description
    triple_quotes = re.compile(r'"""[\S\s]*?"""\n')
    single_comments = re.compile(r"[\s]{4}#\s.+\n")
    inline_comments = re.compile(r'^\s{2}#\s[\S\s]+')
    
    no_comments = re.sub(single_comments, "", code)
    no_inlines = re.sub(inline_comments, "", no_comments)
    no_multiline_strings = re.sub(triple_quotes, "", no_inlines)
    
    return no_multiline_strings
    pass

code = '''
def hello_world():
    # A simple comment preceding a simple print statement
    print("Hello World")
'''

single_comment_after_strip = '''
def hello_world():
    print("Hello World")
'''

print(strip_comments(code))
assert strip_comments(code) == single_comment_after_strip