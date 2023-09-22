# 49-WAP to convert the octal number to decimal number.

n=int(input("Enter any octal number: "))
temp=n
i=0
s=0
while(n>0):
    r=n%10
    s=r*(8**i)+s
    n=n//10
    i+=1
print("Decimal of {} is = {}".format(temp,s))