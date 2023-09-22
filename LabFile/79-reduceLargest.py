# 79-WAP to find the largest element in the given list using reduce() function
from functools import reduce
lst=[3,2,9,6,4,7]
larg=reduce(lambda x,y:x if x>y else y,lst)
print("Largest element in the list is = ",larg)
