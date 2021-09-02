import math
from collections import deque
import queue

class node:
    def __init__(self, val, level):
        self.val = val
        self.level = level

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
    visited = set()
    #count = 1
    
    if math.log2(n).is_integer():
        return int(math.log2(n))
    
    else:
        
        q = queue.Queue()
        nod = node(1, 0)
        q.put(nod)

        while not q.empty():
            # print(queue[-1])
            
            
            current = q.get()
            #print(queue)
            #print(visited)
            
            #print(current.val)
            
            if int(current.val) == int(n):
                print("breaking equal", current.level)
                return current.level
            
            visited.add(current.val)
            
            #print(current.level)
            
            if (current.val * 2) == n or (current.val // 3) == n:
                print("breaking next step", current.level)
                return current.level+1
            
            if (current.val * 2) not in visited:
                nod.val = current.val * 2
                nod.level = current.level + 1
                q.put(nod)
            
            if (current.val // 3) > 1 and (current.val // 3) not in visited:
                nod.val = current.val // 3
                nod.level = current.level + 1
                q.put(nod)
                
            print(list(q.queue))
                
            #count += 1
                
    

print(num_ops(12))    
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