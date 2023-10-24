# 9- Write a program that has a class called Fraction with attributes numerator and denominator.
# a. Write a method called getdata to enter the values of the attributes.
# b. Write a method show to print the fraction in simplified form. 
import math
class Fraction:
    def __init__(self):
        self.getData()
    def getData(self):
        self.num=int(input("Enter the numerator of fraction: "))    
        self.den=int(input("Enter the denominator of the fraction: "))
    def gcd(self,num,den):
        sm=min(num,den)
        while sm>0:
            if num%sm==0 and den%sm==0:
                return sm
            sm-=1
    def show(self):
        g=self.gcd(self.num,self.den)
        if g>1:
            print("Simplified Fraction : {}/{}".format(self.num//g,self.den//g))
        else:
            print("Simplified Fraction : {}/{}".format(self.num,self.den))
    
f=Fraction()
f.show()