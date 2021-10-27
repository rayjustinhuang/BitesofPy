from functools import wraps
from time import time
from typing import Deque, List, Set, Generator
import heapq


def timing(f):
    """A simple timer decorator to print the elapsed time of
       the execution of the function it wraps.
       Returns (timing, result) tuple"""
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()
        duration = end - start
        print(f'Elapsed time {f.__name__}: {duration}')
        return duration, result
    return wrapper


@timing
def contains(sequence: List[int], num: int) -> bool:
    for n in sequence:
        if n == num:
            return True
    return False


@timing
def contains_fast(sequence: Set[int], num: int) -> bool:
    if num in sequence:
        return True
    return False
    pass


@timing
def ordered_list_max(sequence: List[int]) -> int:
    return max(sequence)


@timing
def ordered_list_max_fast(sequence: List[int]) -> int:
    heap_largest = heapq.nlargest(1, sequence)
    return heap_largest
    pass


@timing
def list_concat(sequence: List[str]) -> str:
    bigstr = ''
    for i in sequence:
        bigstr += str(i)
    return bigstr


@timing
def list_concat_fast(sequence: List[str]) -> str:
    pass


@timing
def list_inserts(n: int) -> List[int]:
    lst: List[int] = []
    for i in range(n):
        lst.insert(0, i)
    return lst


@timing
def list_inserts_fast(n: int) -> Deque[int]:
    pass


@timing
def list_creation(n: int) -> List[int]:
    lst = []
    for i in range(n):
        lst.append(i)
    return lst


@timing
def list_creation_fast(n: int) -> Generator[int, None, None]:
    pass