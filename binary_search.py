from string import ascii_lowercase

def binary_search(sequence, target):
    
    if target not in sequence:
        return None
    
    length = len(sequence)
    
    sequence_copy = sequence.copy()
    
    while len(sequence) != 1:
        halfway = int(len(sequence)/2)

        if target < sequence[halfway]:
            sequence = sequence[:halfway]
        else:
            sequence = sequence[halfway:]
    
    answer = sequence[0]
    
    return sequence_copy.index(answer)
    pass