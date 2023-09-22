# 47-WAP to convert the binary number to the decimal number

n=int(input("Enter any binary number: "))
temp=n
i=0
s=0
while(n>0):
    r=n%10
    s=r*(2**i)+s
    n=n//10
    i+=1
print("Decimal of {} is = {}".format(temp,s))