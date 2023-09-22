# 39-WAP to find the sum of odd and even numbers separately within a given range
print("Enter the range to get even and odd")
a=int(input())
b=int(input())

le=[]
lo=[]
for i in range(a,b):
    if i%2==0:
        le.append(i)
    else:
        lo.append(i)
print("Even Numbers: ",le)
print("Odd Numbers: ",lo)