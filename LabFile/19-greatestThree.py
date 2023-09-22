# 19-WAP to find the largest among three numbers.
a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
c=int(input("Enter third number : "))

if a>b:
    if a>c:
        print('{} is greatest number.'.format(a))
    else:
        print('{} is greatest number'.format(c))
else:
    if b>c:
        print('{} is greatest number.'.format(b))
    else:
        print('{} is greatest number.'.format(c))
