# 73-WAP to compute the sum of digits of the given number using recursion 
def digitSum(n):
    if n==0:
        return 0
    return n%10+digitSum(n//10)

n=int(input("Enter any number to find the sum of digit: "))
print("Sum of digit of {} is = {}".format(n,digitSum(n)))