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
        center = int(len(self.ints)/2)
        if not len(self.ints) % 2:
            return (self.ints[center] + self.ints[center-1]) / 2
        else:
            return self.ints[center-1]
            
    def __iadd__(self, new):
        if all([type(i) == int for i in new]):
            return self.ints.append(new)
        else:
            raise TypeError
            
    def __add__(self, new):
        if all([type(i) == int for i in new]):
            return self.ints.append(new)
        else:
            raise TypeError
            
    def append(self, new):
        if type(new) == int:
            return self.ints.append(new)
        else:
            raise TypeError
    pass