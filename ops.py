import math
from collections import deque

def num_ops(n):
    """
    Input: an integer number, the target number
    Output: the minimum number of operations required to reach to n from 1.

    Two operations rules:
    1.  multiply by 2
    2.  int. divide by 3

    The base number is 1. Meaning the operation will always start with 1
    These rules can be run in any order, and can be run independently.

    [Hint] the data structure is the key to solve it efficiently.
    """
    # you code
    ops_num = 0
    target = 1
    start = n
    
    if math.log2(n).is_integer():
        ops_num = math.log2(n)
        return ops_num
    
    else:
        
        queue = deque([1])

        while queue[-1] != n:
            if queue[-1] < n:
                queue.append(queue[-1]*2)
            else:
                queue.append(queue[-1]//3)
                
        ops_num = len(queue)-1
            
    return ops_num
    
    
print(num_ops(10))