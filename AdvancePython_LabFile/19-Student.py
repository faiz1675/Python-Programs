# 19. WAP that create a class Student having attribute as name and age and Marks class inheriting 
# Students class with its own attributes marks1, marks2 and marks3 as marks in 3 subjects. Also, 
# define the class Result that inherits the Marks class with its own attribute total. Every class has 
# its own display() method to display the corresponding details. Use __init__() and super() to 
# implement the above classes

class Student:
    def __init__(self,marks) -> None:
        self.name=input("Enter your name: ")
        self.age=input("Enter your age: ")

    def displayInfo(self):
        print(f"Student Name = {self.name}")
        print(f"Student Age = {self.age}")

class Marks(Student):

    def __init__(self) -> None:
        self.marks1=int(input("Enter marks in the first subject: "))
        self.marks2=int(input("Enter marks in the second subject: "))
        self.marks3=int(input("Enter marks in the third subject: "))
        super().__init__([self.marks1,self.marks2,self.marks3])

    def displayMarks(self):
        print(f"Marks in first subject = {self.marks1}")
        print(f"Marks in second subject = {self.marks2}")
        print(f"Marks in third subject = {self.marks3}")

class Result(Marks):
    def __init__(self,total) -> None:
        self.total=total
        super().__init__()

    def displayResult(self):
        res=(self.marks1+self.marks2+self.marks3)/self.total*100
        print("Result = ",res)

r=Result(300)
r.displayInfo()
r.displayMarks()
r.displayResult()