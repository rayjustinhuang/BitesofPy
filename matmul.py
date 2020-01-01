class Matrix(object):

    def __init__(self, values):
        self.values = values

    def __repr__(self):
        return f'<Matrix values="{self.values}">'
        
    def __matmul__(self, other):
        dot_product = [[0,0],[0,0]]
        for i in range(len(self.values)):
            for j in range(len(other.values)):
                print(self.values[i][j], other.values[j][i])
                dot_product[i][j] += self.values[i][j] * other.values[j][i]
                
        return dot_product
        pass
    
    def __rmatmul__(self, other):
        pass
    
    def __imatmul__(self, other):
        pass
    
mat1 = Matrix([[1, 2], [3, 4]])
mat2 = Matrix([[11, 12], [13, 14]])
mat3 = mat1 @ mat2
"[[37, 40], [85, 92]]"
print(mat3)