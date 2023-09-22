# 59-WAP to compute the P (n, r) using user defined function.
def factorial(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
def NPR(n,r):
    return factorial(n)//factorial(n-r)
n=int(input("Enter the value of n in NPR: "))
r=int(input("Enter the value of r in NPR: "))
npr=NPR(n,r)
print("The value of {}p{} is = {}".format(n,r,npr))