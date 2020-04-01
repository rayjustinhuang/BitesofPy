def count_islands(grid):
    """
    Input: 2D matrix, each item is [x, y] -> row, col.
    Output: number of islands, or 0 if found none.
    Notes: island is denoted by 1, ocean by 0 islands is counted by continously
        connected vertically or horizontically  by '1's.
    It's also preferred to check/mark the visited islands:
    - eg. using the helper function - mark_islands().
    """
    x = len(grid)
    y = len(grid[0])
    
    islands = 0
    for i in range(x):
        for j in range(y):
            if grid[i][j] == 1:
                islands += 1
                mark_islands(i, j, grid)
                pass
    # islands = 0         # var. for the counts
    # .....some operations.....
    # mark_islands(r, c, grid)
    # return islands
    
    return islands


def mark_islands(i, j, grid):
    """
    Input: the row, column and grid
    Output: None. Just mark the visisted islands as in-place operation.
    """
    grid[i][j] = 'X'
    
    try: 
        if grid[i-1][j] == 1:
            grid[i-1][j] = 'X'
    except: pass
    try: 
        if grid[i+1][j] == 1:
            grid[i+1][j] = 'X'
    except: pass
    try: 
        if grid[i][j-1] == 1:
            grid[i][j-1] = 'X'
    except: pass
    try: 
        if grid[i][j+1] == 1:
            grid[i][j+1] = 'X'
    except: pass
    # grid[i][j] = '#'      # one way to mark visited ones - suggestion.