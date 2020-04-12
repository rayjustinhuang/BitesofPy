# Hint:
# You can define a helper funtion: get_others(map, row, col) to assist you.
# Then in the main island_size function just call it when traversing the map.


def get_others(map_, r, c):
    """Go through the map and check the size of the island
       (= summing up all the 1s that are part of the island)

       Input - the map, row, column position
       Output - return the total numbe)
    """
    nums = 0
    # your code here
    rows = len(map_)
    columns = len(map_[0])
    
    starting_cell = map_[r][c]
    
    left, up, down, right = max(c-1,0), max(r-1,0), max(r+1,0), max(c+1,0)
    
    check_left = lambda grid, x, y: grid[x][y-1]
    check_up = lambda grid, x, y: grid[x-1][y]
    check_down = lambda grid, x, y: grid[x+1][y]
    check_right = lambda grid, x, y: grid[x][y+1]
    
    print(map_)
    print(starting_cell)
    print(check_left(map_, r, c))
    
    if starting_cell == 1:
        try:
            if check_up(map_, r, c) != 1:
                nums += 1
        except: nums += 1
    

    return nums


def island_size(map_):
    """Hint: use the get_others helper

    Input: the map
    Output: the perimeter of the island
    """
    perimeter = 0
    # your code here

    return perimeter
    
rectangle = [[0, 1, 1, 0],
             [0, 1, 1, 0],
             [0, 1, 1, 0],
             [0, 1, 1, 0]]

get_others(rectangle, 0, 0)