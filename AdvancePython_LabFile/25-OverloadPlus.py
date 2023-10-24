# 25. Write a program to overload + operator to multiply to fraction object of fraction class which 
# contain two instance variable numerator and denominator. Also, define the instance method 
# simplify() to simplify the fraction objects. 

class Fraction:
    def __init__(self,num=None,den=None) -> None:
        self.num=num
        self.den=den

    def __add__(self,other):
        temp=Fraction()
        temp.num=self.num*other.num
        temp.den=self.den*other.den
        return temp

    def __str__(self) -> str:
        return f"Multiplication by overloading + operator = {self.num},{self.den}" 
    
f1=Fraction(3,5)
f2=Fraction(4,6)
print(f1+f2)