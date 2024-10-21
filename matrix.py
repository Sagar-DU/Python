# Defining a matrix
import numpy as np

matrix = np.array([
    [2, 1, -1], #first row
    [-3, -1, 2], #second row
    [-2, 1, 2] #thrid row
])

# printing the matrix
print (matrix)

# printing the specific element of a matrix 
print ("The row 3 colum 2 element is", matrix[2, 1])

# Transpose of matrix 
print ("Transpose of the matrix is")
print (matrix.T)

def row_echelon (matrix):
    matrix = np.array(matrix, dtype=float)
    rows, cols = matrix.shape

    #go through each column
    for col in range(cols):
        #find the pivot (non-zero element)
        for row in range(col, rows):
            if matrix[row, col] != 0:
                #swap rows if the current pivot is not on the diagonal
                if row != col:  #need to understand this line
                    matrix[[col, row]] = matrix [[row, col]]
                break
        #normalize the pivot row
        pivot = matrix[col, col]
        if pivot != 0:
            matrix[col] = matrix[col] / pivot

        #eleminate the below rows
        for row in range (col + 1, rows):
            multiplier = matrix[row, col]
            matrix[row] -= multiplier * matrix[col]
    return matrix

ref_matrix = row_echelon(matrix)

print ("Row Echelon Form:")
print (ref_matrix)
