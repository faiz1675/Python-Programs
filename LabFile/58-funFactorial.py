# 58-WAP to compute the factorial of the given number using user defined function.
def factorial(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
n=int(input("Enter any number to find factorial: "))
f=factorial(n)
print("Factorial of {} is = {}".format(n,f))