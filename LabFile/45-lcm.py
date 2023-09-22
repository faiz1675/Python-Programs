# 45-WAP to compute the LCM of two numbers
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
maxm=a if a>b else b
while True:
    if maxm%a==0 and maxm%b==0:
        lcm=maxm
        break
    maxm+=1
print("LCM of {} and {} is = {}".format(a,b,lcm))