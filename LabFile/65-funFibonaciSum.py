# 65-WAP to compute the sum of Fibonacci series up to nth term using user defined function

def fibonaciSum(n):
    a,b=0,1
    sum=1
    for i in range(1,n-1):
        s=a+b
        sum+=s
        a=b
        b=s
    return sum
n=int(input("Enter number of terms you want to print fibonacii "))
s=fibonaciSum(n)
print("Sum of {} terms of Fibonacii is = {}".format(n,s))