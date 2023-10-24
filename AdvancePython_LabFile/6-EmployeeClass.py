# 6- Create a class Employee that keeps a track of the number of employees in an organization and 
# also stores their name, designation and salary details.
# a. Write a method called getdata to take input (name, designation, salary) from user. 
# b. Write a method called average to find average salary of all the employees in the organization. 
# c. Write a method called display to print all the information of an employee.


class Employee:
    tot_sal=0
    avg_sal=0
    count=0
    def __init__(self) :
        self.getData()
        Employee.tot_sal+=self.sal
        Employee.count+=1
    def getData(self):
        self.name=input("Enter your name: ")
        self.des=input("Enter your designation: ")
        self.sal=int(input("Enter your salary: "))
    @classmethod
    def average(cls):
        return cls.tot_sal/cls.count
    def display(self):
        print("Your name : ",self.name)
        print("Your designations: ",self.des)
        print("Your salary: ",self.sal)
e1=Employee()
e2=Employee()
e1.display()
e2.display()
print("Average salary of all the employees",Employee.average())