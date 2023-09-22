# 38-WAP to check whether the given number is prime number or not

n=int(input("Enter any number to check prime number: "))
flag=1
for i in range(2,n):
    if n%i==0:
        flag=0
        break
if flag==1:
    print(n, " is a prime number.")
else:
    print(n," is not a prime number")

