import re

def strip_comments(code):
    # see Bite description
    three_indent_docstrings = re.compile(r'[\s]{12}"""[\S\s]*?"""\n')
    class_docstrings = re.compile(r'[\s]{8}"""[\S\s]*?"""\n')
    triple_quotes = re.compile(r'[\s]{4}"""[\S\s]*?"""\n')
    single_comments = re.compile(r"[\s]{4}#\s.+\n")
    inline_comments = re.compile(r'^\s{2}#\s[\S\s]+')
    
    no_three_indents = re.sub(three_indent_docstrings, "", code)
    no_docstrings = re.sub(class_docstrings, "", no_three_indents)
    no_comments = re.sub(single_comments, "", no_docstrings)
    no_inlines = re.sub(inline_comments, "", no_comments)
    no_multiline_strings = re.sub(triple_quotes, "", no_inlines)
    
    return no_multiline_strings
    pass

code = '''
class SimpleClass:
    """Class docstrings go here."""

    def say_hello(self, name: str):
        """Class method docstrings go here."""
        print(f'Hello {name}')

        def func_in_method(self):
            """Docstring with 3 indents and multiline
               should also be stripped
            """
            pass
'''
class_three_indents_after_strip = '''
class SimpleClass:

    def say_hello(self, name: str):
        print(f'Hello {name}')

        def func_in_method(self):
            pass
'''
print(strip_comments(code))
assert strip_comments(code) == class_three_indents_after_strip