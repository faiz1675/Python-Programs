# 56-WAP to check whether the given year is a leap year or not using user defined function
def leapYear(year):
    if year%100==0 and year%400==0:
        return True
    elif year%4==0 and year%100!=0:
        return True
    else:
        return False
y=int(input("Enter any year: "))
if(leapYear(y)):
    print("{} is a Leap Year".format(y))
else:
    print("{} is not a Leap Year".format(y))
