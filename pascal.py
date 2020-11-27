from typing import List


def pascal(N: int) -> List[int]:
    """
    Return the Nth row of Pascal triangle
    """
    # you code ...
    if N == 0:
        return []
    
    triangle_rows = []
    
    for i in range(1, N+1):
        add_row = [None]*i
        add_row[0] = 1
        add_row[-1] = 1
        
        if i == 3:
            add_row[1] = triangle_rows[1][0] + triangle_rows[1][1]
        
        if i >= 4:
            for j in range(1,i-1):
                add_row[j] = triangle_rows[i-2][j-1] + triangle_rows[i-2][j]
                
        
        triangle_rows.append(add_row)
    
    return triangle_rows[N-1]