def binary_search(sequence, target):
    
    length = len(sequence)
    
    sequence_copy = sequence.copy()
    
    #while True:
    while len(sequence) != 1:
        halfway = int(len(sequence)/2)
        
        #if target == sequence[halfway]:
        #    sequence = sequence[halfway]
        #    break
        if target < sequence[halfway]:
            sequence = sequence[:halfway]
        else:
            sequence = sequence[halfway:]
    
    answer = sequence[0]
    
    return sequence_copy.index(answer)
    pass

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
print(binary_search(PRIMES, 59))