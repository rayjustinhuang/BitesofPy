def binary_search(sequence, target):
    
    length = len(sequence)
    
    labeled_sequence = zip(range(length), sequence)
    
    print(list(labeled_sequence))
    
    #while True:
    halfway = int(len(sequence)/2)
    print(halfway)
    
    if target <= sequence[halfway]:
        sequence = sequence[:halfway]
    
    pass

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]

binary_search(PRIMES, 2)