import random

names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
aliases = 'Pythonista Nerd Coder'.split() * 2
points = random.sample(range(81, 101), 6)
awake = [True, False] * 3
SEPARATOR = ' | '


def generate_table(*args):
    rows = zip(*args)
    output = []
    for row in rows:
        delimiter = SEPARATOR
        output.append(delimiter.join(str(x) for x in row))
    return output
    pass