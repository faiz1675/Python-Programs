# 34-WAP to count the number of digits of the given number
n=int(input("Enter any number to compute the total number of digit: "))
temp=n
count=0
while(n>0):
    r=n%10
    count=count+1
    n=n//10
print("Total number of digits in {} is = {}".format(temp,count))