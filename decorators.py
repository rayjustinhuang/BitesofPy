from functools import wraps


def make_html(element):
    def real_decorator(func):
        def wrapped(*args, **kwargs):
            tag_start = "<"+element+">"
            tag_end = "</"+element+">"
            print(tag_start)
            print(func(*args, **kwargs))
            print(tag_end)
        return wrapped
    return real_decorator
    pass

@make_html('p')
@make_html('strong')
def get_text(text='I code with PyBites'):
    return text

print(get_text('I code with PyBites'))