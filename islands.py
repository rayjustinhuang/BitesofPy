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
    
    def check_adjacents(i,j):
        n = [True, True, True, True]
        cells_to_check = [(i,j)]
        while any(n):
            for pair in cells_to_check:
                i = pair[0]
                j = pair[1]
                try: 
                    if grid[i-1][j] == 1:
                        grid[i-1][j] = 'X'
                        n[0] = False
                    else:
                        cells_to_check.append((i-1,j))
                except: pass
                try: 
                    if grid[i+1][j] == 1:
                        grid[i+1][j] = 'X'
                        n[1] = False
                    else:
                        cells_to_check.append((i+1,j))
                except: pass
                try: 
                    if grid[i][j-1] == 1:
                        grid[i][j-1] = 'X'
                        n[2] = False
                    else:
                        cells_to_check,append((i,j-1))
                except: pass
                try: 
                    if grid[i][j+1] == 1:
                        grid[i][j+1] = 'X'
                        n[3] = False
                    else:
                        cells_to_check.append((i,j+1))
                except: pass
    
    #check_adjacents(i,j)
    #check_adjacents(i-1,j)
    #check_adjacents(i+1,j)
    #check_adjacents(i,j-1)
    #check_adjacents(i,j+1)
    # grid[i][j] = '#'      # one way to mark visited ones - suggestion.