from itertools import combinations

def find_number_pairs(numbers, N=10):
    pairs = combinations(numbers, 2)
    
    return [i for i in pairs if sum(i) == N]
    pass