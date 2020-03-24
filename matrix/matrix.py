class Matrix(object):
    def __init__(self, matrix_string):
        self._matrix = [[int(j) for j in x.strip().split(' ')] for x in matrix_string.split('\n')]

    def row(self, index):
        return self._matrix[index - 1]

    def column(self, index):
        return [x[index - 1] for x in self._matrix]