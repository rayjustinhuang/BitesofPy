from itertools import permutations
from operator import add, sub, mul
from typing import List, Union, Iterable


def find_all_solutions(
    operator_path: List[str], expected_result: int
) -> Union[List[List[int]], Iterable[List[int]]]:
    # TODO: blank canvas to fill
    if type(expected_result) != int:
        raise ValueError
    pass

def operation(op: str, expected_result: int):
    if op == '+':
        possible = permutations(range(1,expected_result), 2)
        return [x for x in possible if sum(x) == expected_result]
    possible = permutations(range(1,10),2)
    if op == '-':
        return [x for x in possible if (x[0] - x[1]) == expected_result]
    if op == '*':
        return [x for x in possible if (x[0] * x[1]) == expected_result]
    
    
print(operation('-', 5))