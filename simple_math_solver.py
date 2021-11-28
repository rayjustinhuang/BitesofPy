from itertools import permutations
from operator import add, sub, mul
from typing import List, Union, Iterable


def find_all_solutions(
    operator_path: List[str], expected_result: int
) -> Union[List[List[int]], Iterable[List[int]]]:
    # TODO: blank canvas to fill
    pass

def addition(expected_result: int):
    possible = permutations(range(1,expected_result), 2)
    return [x for x in possible if sum(x) == expected_result]
    
print(addition(6))