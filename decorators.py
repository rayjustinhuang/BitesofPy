from functools import wraps


def make_html(element):
    def real_decorator(func):
        def wrapped(*args):
            tag_start = "<"+element+">"
            tag_end = "</"+element+">"
            text = str(func(*args))
            
            string_to_print = tag_start+text+tag_end
            
            return string_to_print
            
        return wrapped
    return real_decorator
    pass