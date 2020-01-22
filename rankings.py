from dataclasses import dataclass
from typing import List, Tuple

bites: List[int] = [283, 282, 281, 263, 255, 230, 216, 204, 197, 196, 195]
names: List[str] = [
    "snow",
    "natalia",
    "alex",
    "maquina",
    "maria",
    "tim",
    "kenneth",
    "fred",
    "james",
    "sara",
    "sam",
]


@dataclass
class Ninja:
    """
    The Ninja class will have the following features:

    string: name
    integer: bites
    support <, >, and ==, based on bites
    print out in the following format: [469] bob
    """
    def __init__(self,name,bites):
        self.name = name
        self.bites = bites
        
    def __eq__(self, other):
        return self.bites == other.bites
    
    def __lt__(self, other):
        return self.bites < other.bites
        
    def __gt__(self, other):
        return self.bites > other.bites
        
    def __str__(self):
        return f'[{self.bites}] {self.name}'
    pass


@dataclass
class Rankings:
    """
    The Rankings class will have the following features:

    method: add() that adds a Ninja object to the rankings
    method: dump() that removes/dumps the lowest ranking Ninja from Rankings
    method: highest() returns the highest ranking Ninja, but it takes an optional
            count parameter indicating how many of the highest ranking Ninjas to return
    method: lowest(), the same as highest but returns the lowest ranking Ninjas, also
            supports an optional count parameter
    returns how many Ninjas are in Rankings when len() is called on it
    method: pair_up(), pairs up study partners, takes an optional count
            parameter indicating how many Ninjas to pair up
    returns List containing tuples of the paired up Ninja objects
    """
    def __init__(self):
        self._ninja_list = []
    
    def add(self, ninja):
        return self._ninja_list.append(ninja)
        
    def dump(self):
        sorted_list = sorted(self._ninja_list, key=lambda x: x.bites)
        dumped = sorted_list.pop(0)
        return dumped
        
    def highest(self, count=1):
        sorted_list = sorted(self._ninja_list, key=lambda x: x.bites, reverse=True)
        return sorted_list[:count]
    
    def lowest(self, count=1):
        sorted_list = sorted(self._ninja_list, key=lambda x: x.bites)
        return sorted_list[:count]
        
    def len(self):
        return len(self._ninja_list)
    pass