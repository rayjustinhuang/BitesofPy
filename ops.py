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
    start = 1
    
    if math.log2(n).is_integer():
        return int(math.log2(n))
    
    else:
        visited = set()
        
        queue = deque([1]) # 1 is the starting number

        while len(queue) > 0:
            # print(queue[-1])
            
            current = queue.pop()
            
            if current == n:
                return len(queue)
                
            visited.add(current)
            
            if (current * 2) == n or current // 3 == n:
                return len(queue)+1
            
            if (current * 2) not in visited:
                queue.append(current * 2)
            
            if (current // 3) > 1 and (current // 3) not in visited:
                queue.append(current // 3)
                
        ops_num = len(visited)
            
    return ops_num
    

print(num_ops(8))    
print(num_ops(10))
print(num_ops(12))

"""
        queue = deque([1])

        while queue[-1] != n:
            print(queue[-1])
            if queue[-1] < n and queue[-1]*2 not in queue:
                queue.append(queue[-1]*2)
            else:
                queue.append(queue[-1]//3)
                
        ops_num = len(queue)-1
            
    return ops_num
"""