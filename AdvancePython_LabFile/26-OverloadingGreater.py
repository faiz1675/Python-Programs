# 26. Write a program to compare two-person object based on their age by overloading > operator

class Person:
    def __init__(self,age) -> None:
        self.age=age
    
    def __gt__(self,other):
        if self.age>other.age:
            return self.age
        else:
            return other.age
    
p1=Person(24)
p2=Person(18)
print(f"Person with age = {p1>p2} is elder")