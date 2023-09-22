# 40-WAP to display all the prime numbers in given range.
print("Enter the range to print the prime numbers")
a=int(input())
b=int(input())

for j in range(a,b):
    flag=1
    for i in range(2,j):
        if j%i==0:
            flag=0
            break
    if flag==1:
        print(j,end=' ')