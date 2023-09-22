# 80-WAP to find min, max and average of elements of a list having numeric data 
from functools import reduce
lst=[2,3,14,27,1,12,18]
minm=reduce(lambda x,y:x if x<y else y,lst)
maxm=reduce(lambda x,y:x if x>y else y,lst)
s=reduce(lambda x,y:x+y,lst)
avg=s/len(lst)
print("Minimum element of list = ",minm)
print("Maximum element of list = ",maxm)
print("Average of elements of list = ",avg)
