from functools import wraps


DEFAULT_TEXT = ('Subscribe to our blog (sidebar) to periodically get '
                'new PyBites Code Challenges (PCCs) in your inbox')
DOT = '.'


def strip_range(start, end):
    """Decorator that replaces characters of a text by dots, from 'start'
       (inclusive) to 'end' (exclusive) = like range.

        So applying this decorator on a function like this and 'text'
        being 'Hello world' it would convert it into 'Hel.. world' when
        applied like this:

        @strip_range(3, 5)
        def gen_output(text):
            return text
    """
    def real_decorator(func):
        @wraps(func)
        def char_replace(text):
            new_string = ''
            for i in range(len(text)):
                if i >= start and i < 5:
                    new_string += DOT
                else:
                    new_string += text[i]
            return new_string
        return char_replace
    return real_decorator
    pass

#text = 'Hello world'

#@strip_range(3, 5)
#def gen_output(var):
#    return var
    
#print(gen_output(text))