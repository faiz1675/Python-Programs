# 78-WAP to compute the sum of all the elements of the list using reduce() function
from functools import reduce
lst=[3,2,9,6,4,7]
sum=reduce(lambda x,y:x+y,lst)
print("Sum of elements in the list is = ",sum)
