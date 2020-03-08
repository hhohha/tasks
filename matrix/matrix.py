 # task 1 - write a function that takes a list of lists as a parameter and checks if it is a matrix. Matrix has all rows of the same length. Return True or False

def IsItMatrix (matrix):
    if len(matrix) == 0:
        return False
    
    rowLen = len(matrix[0])
    for lst in matrix:
        if len(lst) != rowLen:
            return False
    return True

#print (IsItMatrix ([[1,2,3],[2,3,4],[3,4,5],[4,5,6]]))


# task 2 - write a function that takes a matrix as one parameter and a number as second parameter and adds the number to all elements of the matrix

def matrixPlus (matrix, p):
    i = 0
    while i < len(matrix):
        r = 0
        while r < len (matrix [0]):
            matrix [i][r] += p
            r += 1
        
        i += 1
    return matrix

#matrix = [[1,2,3],[2,3,4],[3,4,5],[4,5,6]]
#tmp = matrixPlus (matrix, 2)
#print (tmp)


# task 3 - write a function that takes a matrix as a parameter and prints it's size

def matrixSize (matrix):
    row = len (matrix)
    colum = len (matrix[0])
    print (row, colum)

#matrixSize ([[1,2,3],[2,3,4],[3,4,5],[4,5,6]])


# task 4 - write a function that performs matrix transposition, example
#                      [1, 5]
#  [1, 2, 3, 4]  ->    [2, 6]
#  [5, 6, 7, 8]        [3, 7]
#                      [4, 8]

def matrixPerforms (matrix):
    c = 0
    matrixNew = []
    while c < len (matrix[0]):
        i = 0
        matrixNewCol = []
        #matrixNew.append ([])
        while i < len (matrix):
            matrixNewCol.append (matrix [i][c])
            #matrixNew[len (matrixNew)-1].append(matrix [i][c])
            i += 1
        matrixNew.append (matrixNewCol)
        c += 1    
    print (matrixNew)
#matrixPerforms ([[1,2,3],[2,3,4],[3,4,5],[4,5,6]])



# task 5 - write function that returns average of all elements of the matrix
def AverageOfMatrix (matrix):
    i = 0
    sumM = 0
    while i < len (matrix):
        j = 0
        while j < len (matrix [i]):
            sumM = matrix [i][j] + sumM
            j += 1
        i += 1
    average = sumM / (  len (matrix[0]) * len (matrix))
    return average

#print (AverageOfMatrix([[1,1,1],[2,2,2],[3,3,3]]))

# task 6 - write function that computes sum of every columns and return sums of columns in a list:
#
#  [1 2 3]
#  [4 5 6]  ->  [12 15 18]
#  [7 8 9]

def sumOfCol (matrix):
    i = 0
    lst = []
    while i < len (matrix):
        sumCol = 0
        j = 0
        while j < len (matrix [0]):
            sumCol = matrix [i][j] + sumCol
            j += 1
        lst.append (sumCol)
        i += 1
    return lst

print (sumOfCol([[1,1,1],[2,2,2],[3,3,3]]))

# task 7 - write a function that takes a square matrix and prints digits on the main diagonal
#  [1 2 3]
#  [4 5 6]  ->  [1 5 9]
#  [7 8 9]
#

# task 8 - write a function that takes a square matrix and prints digits on the second diagonal
#  [1 2 3]
#  [4 5 6]  ->  [3 5 7]
#  [7 8 9]
#
