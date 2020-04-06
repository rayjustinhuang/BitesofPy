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
                x = pair[0]
                y = pair[1]
                
                left = abs(x-1)
                right = abs(x+1)
                up = abs(y-1)
                down = abs(y+1)
                try: 
                    if grid[left][y] == 1:
                        grid[left][y] = 'X'
                        cells_to_check.append((left,y))
                    else:
                        n[0] = False
                except: n[0] = False
                try: 
                    if grid[right][y] == 1:
                        grid[right][y] = 'X'
                        cells_to_check.append((right,y))
                    else:
                        n[1] = False
                except: n[1] = False
                try: 
                    if grid[x][up] == 1:
                        grid[x][up] = 'X'
                        cells_to_check,append((x,up))
                    else:
                        n[2] = False
                except: n[2] = False
                try: 
                    if grid[x][down] == 1:
                        grid[x][down] = 'X'
                        cells_to_check.append((x,down))
                    else:
                        n[3] = False
                except: n[3] = False
                #for i in range(len(grid)):
                #    print(grid[i])
                #print(n)
    
    check_adjacents(i, j)
    
    #check_adjacents(i,j)
    #check_adjacents(i-1,j)
    #check_adjacents(i+1,j)
    #check_adjacents(i,j-1)
    #check_adjacents(i,j+1)
    # grid[i][j] = '#'      # one way to mark visited ones - suggestion.
#circles = [[1, 1, 0, 0, 0, 1],
#           [1, 0, 0, 0, 0, 1],
#           [1, 0, 0, 0, 1, 1],
#           [1, 0, 0, 0, 1, 0],
#           [1, 0, 0, 1, 1, 0],
#           [1, 1, 1, 1, 0, 0]]

#squares = [[1, 1, 0, 1],
#           [1, 1, 0, 1],
#           [0, 0, 1, 1],
#           [1, 1, 1, 0]]
           
#print(count_islands(squares))