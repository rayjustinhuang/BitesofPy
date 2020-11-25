from typing import List


def pascal(N: int) -> List[int]:
    """
    Return the Nth row of Pascal triangle
    """
    # you code ...
    triangle_rows = []
    
    for i in range(1, N+1):
        add_row = [None]*i
        add_row[0] = 1
        add_row[-1] = 1
        
        if i >= 3:
            for j in range(1,i):
                add_row[j] = triangle_rows[i-1][j-1] + triangle_rows[i-1][j]
                
        print(add_row)
        triangle_rows.append(add_row)
    # return row
    print(triangle_rows)

pascal(5)