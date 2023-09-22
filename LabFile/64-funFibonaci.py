# 64-WAP to display the Fibonacci series using user defined function.
def fibonaci(n):
    a,b=0,1
    print(a,b,end=' ')
    for i in range(1,n-1):
        s=a+b
        print(s,end=' ')
        a=b
        b=s
n=int(input("Enter number of terms you want to print fibonacii "))
fibonaci(n)