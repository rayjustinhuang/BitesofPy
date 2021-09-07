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
        output.append(SEPARATOR.join(x for x in row))
    return output
    pass

print(generate_table(names, aliases))