from functools import wraps


def make_html(element):
    def wrapped(func):
        tag_start = "<"+element+">"
        tag_end = "<"+element+"/>"
        print(tag_start+func()+tag_end)
    return wrapped
    pass

@make_html('p')
@make_html('strong')
def get_text(text='I code with PyBites'):
    return text

print(get_text())