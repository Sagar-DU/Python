# Defining a matrix
import numpy as np

matrix = np.array([
    [2, 4, -2], #first row
    [-3, -1, 3], #second row
    [1, 1, 2] #thrid row
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
                if row != col:
                    matrix[[col, row]] = matrix [[row, col]]
                break
        #normalize the pivot row
        pivot = matrix[row, row]
        if pivot != 0:
            matrix[row] = matrix[row] / pivot

        #eleminate the below rows
        for row in range (row + 1, rows):
            multiplier = matrix[row, col]
            matrix[row] -= multiplier * matrix[col]
    return matrix

ref_matrix = row_echelon(matrix)

print ("Row Echelon Form: by numpy")
print (ref_matrix)

import sympy as sp

# Matrix with sympy
matrix = sp.Matrix([[2, 3, -2],
                    [-3, -1, 3],
                    [1, 1, 2]])

# the rref
ref_matrix = matrix.echelon_form()

print ("RREF of the matrix: by sympy")
print (sp.pretty(ref_matrix))
print ("Pivot columns")