class IntList(list):
    
    def __init__(self, ints):
        if all([type(i) == int for i in ints]):
            self.ints = ints
        else:
            raise TypeError
        
    @property
    def mean(self):
        return sum(self.ints)/len(self.ints)
        
    @property
    def median(self):
        if not len(self.ints) % 2:
            return (self.ints[int(len(self.ints)/2)] + self.ints[int(len(self.ints)/2)-1]) / 2
        else:
            return self.ints[int(len(self.ints)/2)-1]
    pass