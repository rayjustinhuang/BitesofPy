class MultiplicationTable:

    def __init__(self, length):
        """Create a 2D self._table of (x, y) coordinates and
           their calculations (form of caching)"""
        self.x = length
        self.y = length
        self._table = ''
        pass

    def __len__(self):
        """Returns the area of the table (len x* len y)"""
        return self.x * self.y
        pass

    def __str__(self):
        """Returns a string representation of the table"""
        for row in self._table:
            print(' | '.join(x for x in row))
        pass

    def calc_cell(self, x, y):
        """Takes x and y coords and returns the re-calculated result"""
        if x > length or y > length:
            raise IndexError
            
        rows = []
        for i in x:
            new_row = [i*j for j in y]
            rows.append(new_row)
            
        self._table = rows
        pass