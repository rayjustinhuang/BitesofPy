class MultiplicationTable:

    def __init__(self, length):
        """Create a 2D self._table of (x, y) coordinates and
           their calculations (form of caching)"""
        self.x = length
        self.y = length
        self._table = self.calc_cell(self.x, self.y)
        pass

    def __len__(self):
        """Returns the area of the table (len x* len y)"""
        return self.x * self.y
        pass

    def __str__(self):
        """Returns a string representation of the table"""
        output = ''
        for row in self._table:
            output += ' | '.join(str(x) for x in row)
            output += "\n"
        
        return output
        pass

    def calc_cell(self, x, y):
        """Takes x and y coords and returns the re-calculated result"""
        if x > self.x or y > self.y:
            raise IndexError
            
        rows = []
        for i in range(1, x+1):
            new_row = [i*j for j in range(1, y+1)]
            rows.append(new_row)
            
        return rows
        pass
    
test = MultiplicationTable(10)
print(test.__len__())
print(test.__str__())