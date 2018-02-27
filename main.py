'''
TODO
1. class Matrix
     - create new matrix
     - fill with  a value
     - print
2. class game
    - create new game
'''

#
# def fill_matrix(x, y, value):
#     matrix[x][y] = value
#
#
# matrix = [[1,2,3,4],[1,1,1,1],[2,2,2,2]]
# fill_matrix(1,1, "valera")
# #print(matrix)


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

testMat = ["-", "-", "-"]



def check_horizontal(matrix, value):
    ''' Checks if matrix has all values in horizontals '''
    res = None
    for line in matrix:
        print("testing line: " + str(line))
        for item in line:
            if item == value:
                res = True
            else:
                res = False
                break
        print ("Result for it: " + str(res))
        if res == True:
            break
    return res


def check_vertical(matrix, value):
    ''' Checks if matrix has all values in verticals '''
    res = None
    for item in range(len(matrix)):
        print ("Testing item " + str(matrix[item]))
        for col in range(len(matrix[item])):
            if matrix[col][item] == value:
                res = True
            else:
                res = False
                break
        print ("Item with index is " + str(res))
        if res == True:
            break
    return res


def is_matrix_square(matrix):
    ''' Checks if matrix is squared'''
    elements_count = len(matrix)
    res = None
    for element in matrix:
        if isinstance(element, list):
            if len(element) == elements_count:
                res = True
            else:
               res = False
               break
        else:
            res = False
            break
    return res


def is_matrix_odd(matrix):
    ''' Checks if matrix is odd or even. Returns TRUE if ODD '''
    if len(matrix) % 2 > 0:
        return False
    return True


def check_diagonals(matrix, value):
    ''' Checks if matrix has all values in diagonals '''
    res = False
    # TODO: Check central value before starting iterations
    # Assuming the list length is equal to each child list length because we will check
    if is_matrix_square(matrix) and not is_matrix_odd(matrix):
        matrix_size = len(matrix)
        # Checking 0,0...3,3
        print("Checking left diagonal")
        for x in range(matrix_size):
            if matrix[0][0] == matrix[x][x] == value:
                res = True
            else:
                res = False
            break
        if res:
            return res
        else:
            # Checking 0,3...3,0
            print("Checking right diagonal")
            for y in reversed(range(matrix_size)):
                for yy in range(matrix_size):
                    if matrix[0][matrix_size-1] == matrix[yy][y] == value:
                        res = True
                    else:
                        res = False
                break
    return res

matx = create_empty_matrix(3, 3)

print(matx)
#fill_with_value(matx, 0, 0, "pony")
#fill_with_value(matx, 1, 1, "pony")
#fill_with_value(matx, 2, 1, "pony")

#print(check_horizontal(matx, "-"))
#print(check_vertical(matx, "-"))
#print(is_matrix_square(matx))
#print(check_diagonals(matx, "-"))


def get_position():
    x = input("X: ")
    y = input("Y: ")
    return int(x), int(y)

def checker(matrix, value):
    if check_horizontal(matrix, value) or check_vertical(matrix, value) or check_diagonals(matrix, value):
        return True


#a = get_position()
#fill_with_value(matx, a[0]-1, a[1]-1, a[2])


while True:
    if not checker(matx,"X"):
        print ("User X turn: ")
        a = get_position()
        fill_with_value(matx, a[0]-1, a[1]-1, "X")
        print(matx)
    else:
        True
        print("X winner")

    if not checker(matx,"O"):
        print ("User O turn: ")
        a = get_position()
        fill_with_value(matx, a[0]-1, a[1]-1, "O")
        print(matx)
    else:
        True
        print("X winner")

print(matx)

