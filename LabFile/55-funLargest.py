# 55-WAP to find the largest of three numbers using user defined function
def largestOfThree(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    return c
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
print("Largest number is = ",largestOfThree(a,b,c))