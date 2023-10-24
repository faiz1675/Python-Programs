# 3- Create a Python class named Rectangle constructed by a length and width. 
# a. Create a method called area which will compute the area of a rectangle.

class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        ar=self.length*self.breadth
        print("Area of rectangle = ",ar)
r=Rectangle(7,12)
r.area()