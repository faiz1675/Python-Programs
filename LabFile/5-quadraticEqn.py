# 5-Python Program to Solve Quadratic Equation using exponent operator
print("Enter the value of a,b and c of any quadratic equation: ")
a=int(input())
b=int(input())
c=int(input())

dis=b**2-4*a*c
if dis<0:
    print("Real roots are not possible for this quadratic equation")
else:
    rdis=dis**0.5
    r1=(-1*b+rdis)/2*a
    r2=(-1*b-rdis)/2*a
    print("The root of the quadratic equation {}x^2 + {}x + {} is = {} and {}".format(a,b,c,r1,r2))