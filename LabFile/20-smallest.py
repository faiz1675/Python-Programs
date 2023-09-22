# 20-WAP to find the smallest among three numbers
a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
c=int(input("Enter second number : "))

if a<b and a<c:
    print(a,' is smallest number.')
elif b<a and b<c:
    print(b,' is smallest number')
else:
    print(c,' is smallest number')
