# 28-WAP to compute the sum of first N natural numbers
n=int(input("Enter the number upto which you  want to display sum of natural numbers"))
s=0
for i in range(1,n+1):
    s=s+i
print("Sum of {} natural numbers = {}".format(n,s))