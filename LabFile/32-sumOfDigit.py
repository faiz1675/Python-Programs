# 32-WAP to compute the sum of the digits of the given number
n=int(input("Enter any number to compute the sum of digit: "))
temp=n
s=0
while(n>0):
    r=n%10
    s=s+r
    n=n//10
print("Sum of digits of {} is = {}".format(temp,s))