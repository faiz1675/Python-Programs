# 7-Create a Python class named Circle constructed by a radius. Use a class variable to define the 
# value of constant PI. 
# a. Write two methods to be named as area and circum to compute the area and the perimeter of a 
# circle respectively by using class variable PI. 
# b. Write a method called display to print area and perimeter.

class Circle:
    PI=3.14
    def __init__(self,r):
        self.r=r
    def area(self):
        ar=Circle.PI*self.r**2
        return ar
    def circum(self):
        crcm=Circle.PI*2*self.r
        return crcm
    def display(self):
        print("Area of circle = ",self.area())
        print("Perimeter of circle = ",self.circum())

r=int(input("Enter radius of the circle: "))
c=Circle(r)
c.display()
