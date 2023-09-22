# 61-WAP to compute the HCF and LCM of two numbers using user defined function
def HCF(a,b):
    minm=min(a,b)
    while(minm>0):
        if a%minm==0 and b%minm==0:
            return minm
        minm=minm-1
def LCM(a,b):
    maxm=max(a,b)    
    while True:
        if maxm%a==0 and maxm%b==0:
            return maxm
        maxm+=1
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
print("LCM of {} and {} is = {}".format(a,b,LCM(a,b)))
print("HCF of {} and {} is = {}".format(a,b,HCF(a,b)))