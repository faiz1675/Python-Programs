# 66-WAP to compute the sum of the digits using user defined function
def sumOfDigit(n):
    s=0
    while n>0:
        r=n%10
        s=s+r
        n=n//10
    return s
n=int(input("Enter any number: "))
print("Sum of digit of {} is = {}".format(n,sumOfDigit(n)))