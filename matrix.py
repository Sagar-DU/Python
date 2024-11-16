# Defining a matrix
matrix = [
    [-2, 3, 5],
    [2, 1, -1]
]

# Printing a matrix 
for i in matrix:
    print (i)

# Accessing each element of the matrix 
index1 = 1
for i in matrix:
    index2 = 1
    for j in i:
        print ("The", index1, index2, "th element is:", j)
        index2 = index2 + 1
    index1 += 1

# Find the order of the matrix 