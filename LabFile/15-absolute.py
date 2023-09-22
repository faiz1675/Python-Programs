# 15-WAP to find the absolute value of the given number.
n=int(input("Enter any number: "))
if n>=0:
    print("Absolute value of {} is = {}".format(n,n))
else:
    print("Absolute value of {} is = {}".format(n,-n))