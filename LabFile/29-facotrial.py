# 29-WAP to compute the factorial of the given number.
n=int(input("Enter the number to find the factorial: "))
f=1
i=n
while(i>=1):
    f=f*i
    i=i-1
print("Factorial of {} is = {}".format(n,f))