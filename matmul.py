class Matrix(object):

    def __init__(self, values):
        self.values = values

    def __repr__(self):
        return f'<Matrix values="{self.values}">'
        
    def __matmul__(self, other):
        dot_product = [[0,0],[0,0]]
        for i in range(len(self.values)):
            for j in range(len(other.values)):
                for k in range(len(self.values)):
                    dot_product[i][j] += self.values[i][k] * other.values[k][j]
                
        return Matrix(dot_product)
        pass
    
    def __rmatmul__(self, other):
        return self.__matmul__(other)
        pass
    
    def __imatmul__(self, other):
        matrix_copy = self.values.copy()
        self.values = [[0,0],[0,0]]
        for i in range(len(self.values)):
            for j in range(len(other.values)):
                for k in range(len(self.values)):
                    #print(matrix_copy[i][k], other.values[k][j])
                    self.values[i][j] += matrix_copy[i][k] * other.values[k][j]
                
        return self
        pass