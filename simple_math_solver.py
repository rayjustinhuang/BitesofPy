from itertools import permutations
from operator import add, sub, mul
from typing import List, Union, Iterable


def find_all_solutions(
    operator_path: List[str], expected_result: int
) -> Union[List[List[int]], Iterable[List[int]]]:
    # TODO: blank canvas to fill
    if type(expected_result) != int:
        raise ValueError
    for o in operator_path:
        if o not in ['+','-','*']:
            raise ValueError
            
    if len(operator_path) == 1:
        return basic_operation(operator_path, expected_result)
    else:
        possible = permutations(range(1, 9), len(operator_path)+1)
        

            
        
    pass

def basic_operation(op: str, expected_result: int):
    if op == '+':
        possible = permutations(range(1,expected_result), 2)
        return [x for x in possible if sum(x) == expected_result]
    possible = permutations(range(1,10),2)
    if op == '-':
        return [x for x in possible if (x[0] - x[1]) == expected_result]
    if op == '*':
        return [x for x in possible if (x[0] * x[1]) == expected_result]
        
def long_operation(op: list, expected_result: int):
    possible = permutations(range(1, 9), len(op)+1)
    
    for answer in possible:
        working_answer = list(answer)
        for operator in op:
        
        # Multiplication first
        if operator == '*':
            mul_index = op.index('*')
            element = mul(working_answer[mul_index], working_answer[mul_index+1])
            working_answer.pop(mul_index)
            working_answer.pop(mul_index)
            working_answer.insert(mul_index, element)
            op.pop(mul_index)
            
        for operator in op:
            
            
    
    
print(operation('-', 5))