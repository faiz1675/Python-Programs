# 54-WAP to check whether the two numbers are equal or not
def checkEqual(a,b):
    return True if a==b else False
n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
if(checkEqual(n1,n2)):
    print("Both the numbers are equal")
else:
    print("Both the numbers are not equal")