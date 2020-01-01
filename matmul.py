class Matrix(object):

    def __init__(self, values):
        self.values = values

    def __repr__(self):
        return f'<Matrix values="{self.values}">'
        
    def __matmul__(self, other):
        dot_product = []
        for j in range(len(other.values)):
            for i in range(len(self.values)):
                dot_product[i][j] = self.values[i] * other.values[j]
        pass
    
    def __rmatmul__(self, other):
        pass
    
    def __imatmul__(self, other):
        pass