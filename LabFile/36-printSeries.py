# 36-WAP to display the following series. 13, -23, 33, - 43, ……., (-1)n+1 n3

n=int(input("Enter any number: "))

for i in range(1,n+1):
    if i%2==0:
        print(-1*i**3,end=' ')
    else:
        print(i**3,end=' ')