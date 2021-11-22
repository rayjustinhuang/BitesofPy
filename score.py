from enum import Enum

THUMBS_UP = '👍'  # in case you go f-string ...

# move these into an Enum:
BEGINNER = 2
INTERMEDIATE = 3
ADVANCED = 4
CHEATED = 1

class Score(Enum):
    BEGINNER = 2
    INTERMEDIATE = 3
    ADVANCED = 4
    CHEATED = 1
    
    # def __init__(self, level):
    #     self.level = level
        
    def __str__(self):
        return f'{self.name} ==> {self.value * THUMBS_UP}'
        
    @classmethod
    def average(cls):
        return sum(x.value for x in cls)/len(cls)
        