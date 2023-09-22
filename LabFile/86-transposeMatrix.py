# 86-Python Program to Transpose a Matrix
lst=[[7,8,15],[5,6,12]]

# trans=[]
# for i in range(len(lst[0])):
#     inTrans=[]
#     for j in lst:
#         inTrans.append(j[i])
#     trans.append(inTrans)
# print(trans)

#By using list Comprehension
y=[[j[i] for j in lst] for i in range(len(lst[0]))]
print(y)
