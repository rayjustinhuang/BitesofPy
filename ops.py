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
    
    while target != start:
        if target < n and target % 3 != 0:
            target *= 2
            ops_num += 1
        else:
            target //= 3
            ops_num += 1
        print(target)

    return ops_num
    
    
print(num_ops(10))