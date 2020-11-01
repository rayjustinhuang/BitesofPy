from typing import List
from collections import defaultdict


def sum_indices(items: List[str]) -> int:
    sum_elements = defaultdict(int)
    
    uniques = set(items)
    
    for char in uniques:
        sum_elements[char] = [i for i in range(len(items)) if items[i] == char]
        
    def sum_sequence(sublist: List[int]):
        result = 0
        for i in range(len(sublist)):
            result += sum(sublist[:i])
            
        return result
        
    total = 0
    
    for key in sum_elements:
        total += sum_sequence(sum_elements[key])
        
    return total
        
test = ['a', 'b', 'b', 'c']

print(sum_indices(test))