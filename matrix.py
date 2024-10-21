# Defining a matrix
import numpy as np

matrix = np.array([
    [2, 5, 1], #first row
    [-2, 6, 3], #second row
    [1, 0, 3] #thrid row
])

# printing the matrix
print (matrix)

# printing the specific element of a matrix 
print ("The row 3 colum 2 element is", matrix[2, 1])

# Transpose of matrix 
print ("Transpose of the matrix is")
print (matrix.T)