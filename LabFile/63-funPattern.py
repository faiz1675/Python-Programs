# 63-WAP to display the pattern using user defined function
def pattern(n):
    for i in range(1,n+1):
        for j in range(1,n+1-i):
            print(' ',end=' ')
        for k in range(1,i+1):
            print("*",end=' ')
        print()

n=int(input("Enter number of rows: "))
pattern(n)
