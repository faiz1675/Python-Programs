# 62-WAP compute the sum of the series using user defined function.

def seriesSum(n):
    sum=0
    for i in range(1,n+1):
        sum+=2*i
    return sum
n=int(input("Enter the number of terms: "))
print("Sum of series = ",seriesSum(n))