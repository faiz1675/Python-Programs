# 22-WAP to check whether a given year is leap year or not
y=int(input("Enter any year to check leap year or not: "))

if y%4==0 and y%100!=0:
    print("{} is a leap year".format(y))
elif y%4==0 and y%400==0:
    print("{} is a leap year".format(y))
else:
    print("{} is not a leap year".format(y)) 
