# 22. Write a program that has a class Polygon. Derive two classes Rectangle and triangle from 
# polygon and write methods to get the details of their dimensions and hence calculate the area.

from abc import ABC,abstractmethod

class Polygon(ABC):
    def __init__(self,length) -> None:
        self.length=length
    @abstractmethod
    def getDetails(self):
        pass
    @abstractmethod
    def area(self):
        pass

class Rectangle(Polygon):
    def __init__(self,length,breadth) -> None:
        super().__init__(length)
        self.breadth=breadth

    def getDetails(self):
        print("Length of the rectangle is = ",self.length)
        print("Breadth of the rectangle is = ",self.breadth)
    
    def area(self):
        ar=self.length*self.breadth
        print(f"Area of Rectangle = {ar}")

class Triangle(Polygon):
    def __init__(self, length,base) -> None:
        super().__init__(length)
        self.base=base
    
    def getDetails(self):
        print("Base of the triagnle is = ",self.base)
        print("Height of the triangle is = ",self.length)

    def area(self):
        ar=0.5*self.length*self.base
        print(f"Area of Triangle = {ar}")

l=int(input("Enter length of the rectangle: "))
b=int(input("Enter breadth of the rectangle: "))
r=Rectangle(l,b)
r.getDetails()
r.area()
base=int(input("Enter length of the rectangle: "))
ht=int(input("Enter length of the rectangle: "))
t=Triangle(ht,base)
t.getDetails()
t.area()