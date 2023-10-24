# 18- Write a program that has a class Point. Define another class Location which has two objects 
# (Location and destination) of class Point. Also, define a function in Location that prints the 
# reflection on the y-axis.

class Point:
    def __init__(self,x,y) -> None:
        self.x=x
        self.y=y

class Location(Point):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)

    def location(self):
        print(f"Reflaction on y-axis = ({-self.x},{self.y})")

    def destination(self):
        d=(self.x**2+self.y**2)**0.5
        print(f"Destination from origin = {d}")

print("Enter the co-ordinate point: ")
x,y=map(int, input().split())
p=Location(x,y)
p.location()
p.destination()