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
    visited1 = set()
    visited2 = set()
    
    if math.log2(n).is_integer():
        return int(math.log2(n))
    
    else:
        
        queue1 = deque([1]) # 1 is the starting number
        queue2 = deque([1])

        while len(queue1) > 0:
            # print(queue[-1])
            
            current1 = queue1.pop()
            current2 = queue2.pop()
            
            if current1 == n:
                return len(queue1)
            if current2 == n:
                return len(queue2)
                
            visited1.add(current1)
            visited2.add(current2)
            
            if (current1 * 2) == n or current1 // 3 == n:
                return len(queue1)+1
            
            if (current2 * 2) == n or current2 // 3 == n:
                return len(queue2)+1
            
            if (current1 * 2) not in visited1:
                queue1.append(current1 * 2)
            
            if (current2 // 3) > 1 and (current2 // 3) not in visited2:
                queue2.append(current2 // 3)
    

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