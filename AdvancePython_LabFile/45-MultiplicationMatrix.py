#45-Write a Numpy program to calculate the multiplication of the two matrices

import numpy as np

row1=int(input("Enter the row of the first matrix: "))
col1=int(input("Enter the column of the first matrix: "))
row2=int(input("Enter the row of the second matrix: "))
col2=int(input("Enter the column of the second matrix: "))

if col1==row2:
    matrix1=np.zeros((row1,col1))
    matrix2=np.zeros((row2,col2))
    print("Enter the elements for the first matrix:")
    for i in range(row1):
        for j in range(col1):
            a=int(input(f"Enter the element at position Matrix{i+1}{j+1}: "))
            matrix1[i][j]=a
    
    print("Enter the elements for the second matrix:")
    for i in range(row2):
        for j in range(col2):
            a=int(input(f"Enter the element at position Matrix{i+1}{j+1}: "))
            matrix2[i][j]=a
    
    print(np.dot(matrix1,matrix2))

else:
    print("Multiplication of the given two matrices is not possible")