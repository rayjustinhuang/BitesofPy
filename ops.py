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
    start = set()
    visited = set()
    count = 1
    
    if math.log2(n).is_integer():
        return int(math.log2(n))
    
    else:
        
        queue = {1: 1} # 1 is the starting number

        while len(queue) > 0:
            # print(queue[-1])
            
            
            current = list(queue.keys())[-1]
            #print(queue)
            #print(visited)
            
            if n in queue:
                return queue[n]
            
            #if (current * 2) == n or current // 3 == n:
            #    return queue[n]+1
            
            if (current * 2) not in visited:
                visited.add(current * 2)
                queue[current * 2] = count
            
            if (current // 3) > 1 and (current // 3) not in visited:
                visited.add(current // 3)
                queue[current // 3] = count
                
            count += 1
                
    

print(num_ops(15))    
#print(num_ops(10))
#print(num_ops(12))

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