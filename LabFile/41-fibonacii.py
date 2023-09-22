# 41-WAP to compute the sum of Fibonacci series up to nth term.

n=int(input('Enter number of terms you want to print the fibonaccii: '))

a,b=0,1
print(a,b,end=' ')

for i in range(2,n):
    s=a+b
    print(s,end=' ')
    a=b
    b=s
    
