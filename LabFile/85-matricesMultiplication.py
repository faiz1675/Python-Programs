# 85-Python Program to Multiply Two Matrices

def multiply_matrices(matrix1, matrix2):
    # Check if the matrices can be multiplied
    if len(matrix1[0]) != len(matrix2):
        return None

    # Create a result matrix with appropriate dimensions
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

    # Perform matrix multiplication
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result


# Example usage
matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8], [9, 10], [11, 12]]

result = multiply_matrices(matrix1, matrix2)

if result is not None:
    print("The product of the matrices is:")
    for row in result:
        print(row)
else:
    print("The matrices cannot be multiplied.")