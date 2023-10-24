# 23. Write a program that extends the class Shape to calculate the area of a circle and a cone .(use 
# super to inherit base class methods)

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self) -> None:
        self.r=int(input("Enter radius of circle: "))
    def area(self):
        ar=3.14*self.r**2
        return ar

class Cone(Circle):
    def __init__(self) -> None:
        self.r=int(input("Enter the radius of a cone: "))
        self.h=int(input("Enter the height of a cone: "))
    def area(self):
        # basear=3.14*self.r**2
        basear=super().area()
        l=(self.r**2+self.h**2)**0.5
        lsar=3.14*self.r*l
        return basear+lsar
    
# c=Circle()
# print("Area of circle = ",c.area())
cone=Cone()
print("Area of cone = ",cone.area())
