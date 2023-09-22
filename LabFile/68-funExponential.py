# 68-WAP to compute the exponential of number w.r.t. another number
def exponential(x,n):
    if n==0:
        return 1
    e=1
    for i in range(1,n+1):
        e=x*e
    return e

print("Enter the base and power: ")
x=int(input())
n=int(input())
print(exponential(x,n))