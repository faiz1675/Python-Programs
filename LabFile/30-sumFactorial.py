# 30-WAP to compute the sum of factorial of the first n natural number
n=int(input("Enter the number to find the sum of factorial: "))
s=0
for i in range(1,n+1):
    f=1
    while(i>=1):
        f=f*i
        i=i-1
    s=s+f
print("Sum of Factorial of {} natural number is = {}".format(n,s))