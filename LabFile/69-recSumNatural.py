# 69-WAP to compute the sum of the first n natural number using recursion.
def sumOfNatural(n):
    if n==0:
        return 0
    return n+sumOfNatural(n-1)
n=int(input("Enter any number: "))
print("Sum of {} natural numbers is = {}".format(n,sumOfNatural(n)))