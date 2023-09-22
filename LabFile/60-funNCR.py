# 60-WAP to compute the C (n, r) using the user defined function.
def factorial(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
def NCR(n,r):
    return factorial(n)//(factorial(r)*factorial(n-r))
n=int(input("Enter the value of n in NCR: "))
r=int(input("Enter the value of r in NCR: "))
ncr=NCR(n,r)
print("The value of {}c{} is = {}".format(n,r,ncr))