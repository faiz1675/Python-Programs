# 18-WAP to check whether a number is divisible by another number
a=int(input("Enter first number i.e Dividend : "))
b=int(input("Enter second number i.e Divisor : "))

if a%b==0:
    print('{} is completly divisible by {}'.format(a,b))    
else:
    print('{} is not completly divisible by {}'.format(a,b))