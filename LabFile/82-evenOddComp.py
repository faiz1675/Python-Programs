# 82-WAP to find sum of all even numbers and odd numbers separately in a list 
from functools import reduce
lst=[2,3,4,5,6,7,8]

odd=[i for i in lst if i%2!=0]
sumOdd=reduce(lambda x,y:x+y,odd)
even=[i for i in lst if i%2==0]
sumEven=reduce(lambda x,y:x+y,even)
print("List of odd numbers: ",odd)
print("List of even numbers: ",even)
print("Sum of elements of odd elements in the list: ",sumOdd)
print("Sum of elements of even elements in the list: ",sumEven)