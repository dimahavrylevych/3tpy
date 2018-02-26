'''
TODO
1. class Matrix
     - create new matrix
     - fill with  a value
     - print
2. class game
    - create new game
'''


def fill_matrix(x, y, value):
    matrix[x][y] = value


matrix = [[1,2,3,4],[1,1,1,1],[2,2,2,2]]
fill_matrix(1,1, "valera")
#print(matrix)


def create_empty_matrix(x, y):
    mat = []
    for item in range(x):
        mat += [[]]
    for nest in mat:
        for elem in range(y):
            nest.append("-")
    return mat

def fill_with_value(matrix, x, y, value):
    matrix[x][y] = value
    return matrix


matx = create_empty_matrix(3, 3)
print(matx)
#fill_with_value(matx, 1, 1, "pony")
print(matx)
