# 26-WAP to simulate the calculator (Arithmetic operations: +, -, /, *).
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))

ch=input("Enter the operator to perform the aritmetic operation: ")

if ch=='+':
    print(a+b)
elif ch=='-':
    print(a-b)
elif ch=='*':
    print(a*b)
elif ch=='/':
    print(a/b)
else:
    print("Please enter the correct operator")