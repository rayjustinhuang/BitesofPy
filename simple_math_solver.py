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
        return basic_operation(operator_path[0], expected_result)
    else:
        return long_operation(operator_path, expected_result)
        

            
        
    pass

def basic_operation(op: str, expected_result: int):
    if op == '+':
        possible = permutations(range(1,9), 2)
        return [list(x) for x in possible if sum(x) == expected_result]
    possible = permutations(range(1,10),2)
    if op == '-':
        return [list(x) for x in possible if (x[0] - x[1]) == expected_result]
    if op == '*':
        return [list(x) for x in possible if (x[0] * x[1]) == expected_result]
        
def long_operation(op: list, expected_result: int):
    possible = permutations(range(1, 9), len(op)+1) # [[6, 7, 8, 9, 4, 5, 2]] 
    
    allowed_answers = []
    
    for answer in possible:
        working_answer = list(answer)
        list_of_ops = list(op)
        
        if '*' in list_of_ops:
            final_answer = [ working_answer[list_of_ops.index('*')] ] * len(working_answer)
        else:
            final_answer = [ working_answer[0] ] * len(working_answer)
            
        #print(final_answer)
            

        for operator in list_of_ops:
            
            #print(operator)
            #print('looping')
        
            # Multiplication first
            if operator == '*':
                mul_index = list_of_ops.index('*')
                element = mul(final_answer[mul_index], working_answer[mul_index+1])
                final_answer = [ element ] * len(working_answer)
                #working_answer.pop(mul_index)
                #working_answer.insert(mul_index, element)
                #list_of_ops.pop(mul_index)
            else:
                continue
            
            #print(final_answer)
            #print(working_answer)

        new_list_of_ops = [x for x in list_of_ops] #if x != '*']
            
        for operator in new_list_of_ops:
            
            if operator == '+':
                add_index = new_list_of_ops.index('+')
                #print(add_index)
                element = add(final_answer[add_index], working_answer[add_index+1])
                final_answer = [ element ] * len(working_answer)
                #working_answer.pop(add_index)
                #working_answer.insert(add_index, element)
                #list_of_ops.pop(add_index)

            elif operator == '-':
                sub_index = new_list_of_ops.index('-')
                if new_list_of_ops[sub_index-1] == '*':
                    element = sub(working_answer[sub_index], final_answer[sub_index+1])
                else:
                    element = sub(final_answer[sub_index], working_answer[sub_index+1])
                final_answer = [ element ] * len(working_answer)
                #working_answer.pop(sub_index)
                #working_answer.insert(sub_index, element)
                #list_of_ops.pop(sub_index)

            else:
                continue
            
            print(final_answer)
        
        #print(working_answer)
        #print(list_of_ops)
        
        if final_answer[0] == expected_result:
            allowed_answers.append(list(answer))
            
    return allowed_answers
            
    
    
#print(basic_operation('-', 6))
#print(long_operation(['*','*','+'],181))
#print(find_all_solutions(['*','-'], 16))
#print(find_all_solutions(['+'], 6))
#print(find_all_solutions(['+', '*', '*', '+', '*', '-'], 528))
#print(find_all_solutions(['-', '*'], -16))
