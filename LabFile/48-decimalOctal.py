# 48-WAP to convert the decimal number to the octal number
n=int(input("Enter any decimal number to find the octal: "))
octal=""
temp=n
while n>0:
    octal=str(n%8)+octal
    n=n//8
print("Octal of {} is = {}".format(temp,octal))