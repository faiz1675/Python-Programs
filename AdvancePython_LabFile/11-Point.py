# 11- Write a program that has a class Point with attributes x and y. 
# a. Write a method called midpoint that returns a midpoint of a line joining two points. 
# b. Write a method called length that returns the length of a line joining two points. 

class Point:
    def __init__(self,x=None,y=None) -> None:
        self.x=x
        self.y=y
    def midpoint(self,other):
        temp=Point()
        temp.x=(self.x+other.x)/2
        temp.y=(self.y+other.y)/2
        # return temp
        return temp.x,temp.y
    
    def length(self,other):
        l=((self.x-other.x)**2+(self.y-other.y)**2)**0.5
        return l

print("Enter the co-ordinates of first point: ")
x1,y1=map(int, input().split())    
p1=Point(x1,y1)
print("Enter the co-ordinates of second point: ")
x2,y2=map(int, input().split())
p2=Point(x2,y2)
# print(p1.midpoint(p2))
print("Mid Point = ",p1.midpoint(p2))
print("Length between two points = ",p1.length(p2))