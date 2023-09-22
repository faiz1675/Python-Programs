# 70-WAP to compute the factorial of the given number using recursion
def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)

n=int(input("Enter any number: "))
print("Factorial of {} is = {}".format(n,factorial(n)))