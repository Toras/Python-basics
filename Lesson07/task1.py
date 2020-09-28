class Matrix:
    matrix = [[0]]

    def __init__(self, matrix):
        self.matrix = matrix
    
    def __str__(self):
        st = ''
        for i in range(0, len(self.matrix)):
            st = st + ' '.join(map(str, (self.matrix[i]))) + '\n'
        return st
    
    def __add__(self, other):
        r_matrix = []
        for i in range(len(self.matrix)):
            r_matrix.append([])
            for j in range(len(self.matrix[i])):
                r_matrix[i].append(self.matrix[i][j] + other.matrix[i][j])
        return Matrix(r_matrix)


m_1 = Matrix([[2, 3, 6], [5, 6, 1]])
m_2 = Matrix([[8, 32, 765], [5, 65, 21]])
print(f'{m_1}{m_2}')
print(m_1 + m_2)
