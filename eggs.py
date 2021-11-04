from random import choice

COLORS = 'red blue green yellow brown purple'.split()


class EggCreator:
    def __init__(self, limit):
        self.limit = limit
        
    def __iter__(self):
        self.count = 0
        return self
        
    def __next__(self):
        if self.count <= self.limit:
            return choice(colors) + 'egg'
        else:
            raise StopIteration
    pass