# 67-WAP to check whether the given number is a prime number or not using user defined
# function.
def checkPrime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

n=int(input("Enter any number: "))
if(checkPrime(n)):
    print(n, "is a Prime Number")
else:
    print(n, "is not a Prime Number")