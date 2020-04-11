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
    
    starting_cell = map[r][c]
    
    check_up = lambda grid, x, y: grid[x][y-1]
    check_left = lambda grid, x, y: grid[x-1][y]
    check_right = lambda grid, x, y: grid[x+1][y]
    check_down = lambda grid, x, y: grid[x][y+1]
    
    

    return nums


def island_size(map_):
    """Hint: use the get_others helper

    Input: the map
    Output: the perimeter of the island
    """
    perimeter = 0
    # your code here

    return perimeter