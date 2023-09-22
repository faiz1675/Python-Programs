# 72-WAP to display the Fibonacci series using recursion
def fibonaci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    return fibonaci(n-1)+fibonaci(n-2)

n=int(input("Enter the number of terms: "))
for i in range(1,n):
    print(fibonaci(i),end=' ')