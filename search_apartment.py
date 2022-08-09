from typing import List

EAST = "E"
WEST = "W"


def search_apartment(buildings: List[int], direction: str) -> List[int]:
    """
    Find and return the indices of those building with
    the desired view: EAST (E) or WEST (W).

    See sample inputs / outputs below and in the tests.
    """
    desired = []
    
    if direction == 'W':
        for b in range(len(buildings)):
            if b == 0:
                desired.append(buildings[b])
            else:
                active = desired[-1]
                if buildings[b] >= active:
                    desired.append(buildings[b])
                else:
                    continue
                continue
        
    else:
        for b range(len(buildings), step=-1):
            if b == len(buildings):
                desired.append(buildings[b])
            else:
                active = desired[-1]
                if buildings[b] >= active:
                    desired.append(buildings[b])
                else:
                    continue
                continue


if __name__ == "__main__":
    A = [3, 5, 4, 4, 7, 1, 3, 2]  # central tallest
    B = [1, 1, 1, 1, 1, 2]  # almost flat
    #
    #  W <-                    ->  E(ast)
    #
    print(search_apartment(A, "W"))  # [0, 1, 4]
    print(search_apartment(A, "E"))  # [4, 6, 7]
    print(search_apartment(B, "W"))  # [0, 5]
    print(search_apartment(B, "E"))  # [5]