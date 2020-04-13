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
    rows, cols = len(map_), len(map_[0])
    
    starting_cell = map_[r][c]
    
    dirs = [[-1, 0], [0, 1], [0, -1], [1, 0]]

    for dir in dirs:
        nr, nc = r + dir[0], c + dir[1]
        if nr >= 0 and nc >= 0 and nr < rows and nc < cols:
            if map_[nr][nc] != 1:
                nums += 1
    
    print(map_)
    print(starting_cell)
    print(nums)

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

get_others(rectangle, 0, 1)