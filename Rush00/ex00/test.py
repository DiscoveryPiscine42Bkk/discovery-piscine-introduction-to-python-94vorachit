#!/usr/bin/env python3

import numpy as np
import re

# Example arrays
array1 = np.array(['a', 'b', 'c'])
array2 = np.array(['d', 'f', 'g'])
array3 = np.array(['h', 'i', 'j'])

# Concatenate arrays
combined_array = np.concatenate((array1, array2, array3))
#print(combined_array)
#print(combined_array[1])
# Reshape to a matrix (e.g., 3x3)
matrix1 = combined_array.reshape((3, 3))

# Print the matrix and its shape
print("Matrix:\n", matrix1)
print(matrix1[0,0])
#print("Matrix shape:", matrix1.shape)

def is_square_matrix(matrix):
    """
    Checks if a given matrix is a square matrix.

    Args:
        matrix: A list of lists representing the matrix.

    Returns:
        True if the matrix is square, False otherwise.
    """
#    if not matrix:
#        print("False")#return False  # Empty matrix is not considered square

    num_rows = len(matrix)
    for row in matrix:
        if len(row) != num_rows:
            print("False")#return False
    print("True")#return True

#print(f"Matrix 1 is square: {is_square_matrix(matrix1)}")
#is_square_matrix(matrix1)
character = ['.','P','B','R','Q','K']
#print(character)
#a = input("Type something :")
#a1 = list(a)
#print(a)
#print(a1)
#for arg1 in a1:
#    if arg1 not in character:
#        print("Flase")
#print(len(a))
#b = input("Type somthong :")
#b1 = list(b)
#if len(a) != len(b):
#    print()
#b = input("type something :")
#b1 = list(b)
#c = input("type something :")
#c1 = list(c)
#print(combined_array)
#matrix2 = combined_array2.reshape((3, 3))
#print(matrix2)
