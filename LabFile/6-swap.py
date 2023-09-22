# 6-Python Program to Swap Two Variables
a=int(input('Enter first number: '))
b=int(input('Enter second number: '))
print("Before Swapping:")
print("First Number = {} and Second Number = {}".format(a,b))

a=a+b
b=a-b
a=a-b
print("After Swapping:")
print("First Number = {} and Second Number = {}".format(a,b))
