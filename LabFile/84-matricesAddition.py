# 84-Python Program to Add Two Matrices 

def addMatrix(matrix1,matrix2):
    if len(matrix1)!=len(matrix2) or len(matrix1[0])!=len(matrix2[0]):
        return None
    
    #creating a resultant matrix to store the addition of matrix
    result=[[0 for i in range(len(matrix1[0]))]for i in range(len(matrix1))]

    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j]=matrix1[i][j]+matrix2[i][j]
    return result

m1=[[2,3,5],[7,4,6]]
m2=[[9,8,2],[5,6,8]]
# mulAddition=addMatrix(m1,m2)

# if mulAddition!=None:
#     print("Addition of the given two matrices:")
#     for row in mulAddition:
#         print(row)
# else:
#     print("Order of the two matrices are not same, therefore addition not possible")


#Using list comprehension
result=[[m1[i][j]+m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]
print(result)