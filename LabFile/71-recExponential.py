# 71-WAP to compute the exponential of number w.r.t. another number using recursion 
def exponent(x,n):
    if n==0:
        return 1
    return x*exponent(x,n-1)
x,n=5,4
print(exponent(x,n))