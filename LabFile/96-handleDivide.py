# 96-Python Program to handle divide by zero exception.
a=int(input("Enter first number i.e. dividend: "))
b=int(input("Enter second number i.e. divisor: "))
try:
    print(a/b)
except ZeroDivisionError as obj:
    print("You can't divide by zero",obj)