# 35-WAP to check whether the given number is an Armstrong number or not
n=int(input("Enter any number to check Armstrong or not: "))
l=len(str(n))
temp=n
s=0
while(n>0):
    r=n%10
    s=s+r**l
    n=n//10
if s==temp:
    print("{} is an Armstron number".format(temp))
else:
    print("{} is not an Armstrong number".format(temp))