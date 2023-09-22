# 46-WAP to convert the decimal number to the binary number
n=int(input("Enter any number to find the binary: "))
# print(bin(n)[2:])     #binary conversion using built in function
b=""
temp=n
while n>0:
    b=str(n%2)+b
    n=n//2
print("Binary of {} is = {}".format(temp,b))