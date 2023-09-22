# 44-WAP to compute the HCF of two numbers.
a=int(input("Enter first number"))
b=int(input("Enter second number"))

smaller=a if a<=b else b

while(smaller>0):
    if a%smaller==0 and b%smaller==0:
        print("HCF of {} and {} is = {}".format(a,b,smaller))
        break
    smaller-=1
