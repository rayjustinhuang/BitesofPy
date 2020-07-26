import string
import itertools

def sequence_generator():
    numbers = range(1,27)
    letters = list(string.ascii_uppercase[:27])
    
    combined = []
    for num, let in zip(numbers, letters):
        combined.append(num)
        combined.append(let)
    
    return itertools.cycle(combined)
    pass